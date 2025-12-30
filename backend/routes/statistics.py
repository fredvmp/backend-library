from flask import Blueprint, jsonify
from db.connection import get_connection

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
            COUNT(DISTINCT rsh.user_id) AS times_readed
        FROM books b
        JOIN reading_status_history rsh ON b.id = rsh.book_id
        JOIN authors a ON b.author_id = a.id
        WHERE rsh.status = 'FINISHED'
        GROUP BY b.id, b.title, author
        ORDER BY times_readed DESC
    """

    cur.execute(query)
    rows = cur.fetchall()

    books = []

    for row in rows:

        books.append({
            "book_id": row[0],
            "book_title": row[1],
            "author": row[2],
            "times_readed": row[3]
        })
    
    cur.close()
    conn.close()

    return jsonify(books)
        




