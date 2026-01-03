from flask import Blueprint, jsonify
from db.queries.books_queries import fetch_books, fetch_books_with_rating


books_bp = Blueprint("books", __name__, url_prefix="/books")

# Obtener todos los libros y su escritor


@books_bp.route("/", methods=["GET"])
def get_books():

    rows = fetch_books()

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

    rows = fetch_books_with_rating()

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
