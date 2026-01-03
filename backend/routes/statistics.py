from flask import Blueprint, jsonify, request
from db.connection import get_connection
from datetime import date, datetime
import psycopg2

statistics_bp = Blueprint("statistics", __name__, url_prefix="/statistics")


@statistics_bp.route("/most-read-books", methods=["GET"])
def get_most_read_books():

    conn = get_connection()
    cur = conn.cursor()

    query = """
        SELECT 
            b.id, 
            b.title, 
            a.name AS author, 
            COUNT(DISTINCT rsh.user_id) AS times_read
        FROM books b
        JOIN reading_status_history rsh ON b.id = rsh.book_id
        JOIN authors a ON b.author_id = a.id
        WHERE rsh.status = 'FINISHED'
        GROUP BY b.id, b.title, author
        ORDER BY times_read DESC
    """

    cur.execute(query)
    rows = cur.fetchall()

    books = []

    for row in rows:

        books.append({
            "book_id": row[0],
            "book_title": row[1],
            "author": row[2],
            "times_read": row[3]
        })

    cur.close()
    conn.close()

    return jsonify(books)

# Libros finalizados en un rango de fechas concreto

@statistics_bp.route("/readed-books-specific-date", methods=["GET"])
def get_readed_books_in_specific_date():

    conn = None
    cur = None

    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")

    if not start_date:
        return jsonify({
            "error": "start_date is required (yyyy-mm-dd)"
        }), 400

    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = (
            datetime.strptime(end_date, "%Y-%m-%d").date()
            if end_date
            else date.today()
        )
    except ValueError:
        return jsonify({
            "error": "Invalid date format. Use yyyy-mm-dd"
        }), 400

    try:
        conn = get_connection()
        cur = conn.cursor()

        query = """
            SELECT 
                b.id,
                b.title,
                a.name AS author,
                ARRAY_AGG(DISTINCT g.name) AS genres,
                rsh.status_date AS ending_date
            FROM books b
            JOIN book_genres bg ON b.id = bg.book_id
            JOIN genres g ON g.id = bg.genre_id
            JOIN authors a ON b.author_id = a.id
            JOIN reading_status_history rsh ON b.id = rsh.book_id
            WHERE rsh.status = 'FINISHED'
                AND rsh.status_date BETWEEN %s AND %s
            GROUP BY b.id, b.title, a.name, rsh.status_date
            ORDER BY rsh.status_date DESC;
        """

        cur.execute(query, (start_date, end_date))
        rows = cur.fetchall()

        books = []
        for row in rows:
            books.append({
                "book_id": row[0],
                "book_title": row[1],
                "author": row[2],
                "genres": row[3],
                "ending_date": row[4].isoformat()
            })

        return jsonify({
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
            "results": books
        })

    except psycopg2.Error:  # errores bbdd
        return jsonify({
            "error": "Database error"
        }), 500

    except ValueError:  # errores de formato
        return jsonify({
            "Invalid data format. Dates must be yyyy-mm-dd"
        })

    except Exception as e:  # errores inesperados
        return jsonify({
            "error": "Internal server error",
        }), 500

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
