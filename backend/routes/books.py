from flask import Blueprint, jsonify
from db.connection import get_connection

books_bp = Blueprint("books", __name__, url_prefix="/books")

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






