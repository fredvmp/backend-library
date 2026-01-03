from flask import Blueprint, jsonify
from db.connection import get_connection

books_bp = Blueprint("books", __name__, url_prefix="/books")

# Obtener todos los libros y su escritor

@books_bp.route("/", methods=["GET"])
def get_books():

    conn = get_connection()
    cur = conn.cursor()

    query = """
        SELECT
            b.id,
            b.title,
            a.name AS author
        FROM books b
        JOIN authors a ON b.author_id = a.id
        ORDER BY b.id;
    """

    cur.execute(query)
    rows = cur.fetchall()

    cur.close()
    conn.close()

    books = []
    for row in rows:
        books.append({
            "id": row[0],
            "title": row[1],
            "author": row[2]
        })

    return jsonify(books)

# Obtener los libros y la media de su puntuación

@books_bp.route("/ratings", methods=["GET"])
def get_books_with_rating():

    conn = get_connection()
    cur = conn.cursor()

    query = """
        SELECT
            b.id,
            b.title,
            a.name AS author,
            ROUND(AVG(r.score), 2) AS average_rating,
            COUNT(r.score) AS total_ratings
        FROM books b
        JOIN authors a ON b.author_id = a.id
        JOIN ratings r ON r.book_id = b.id
        GROUP BY b.id, b.title, a.name
        ORDER BY average_rating DESC;
    """

    cur.execute(query)
    rows = cur.fetchall()

    cur.close()
    conn.close()

    books = []
    for row in rows:
        books.append({
            "book_id": row[0],
            "title": row[1],
            "author": row[2],
            "average_rating": row[3],
            "total_ratings": row[4]
        })

    return jsonify(books)
