from flask import Blueprint, jsonify, request
import psycopg2
from db.queries.books_queries import fetch_most_read_books
from db.queries.books_queries import fetch_books, fetch_books_with_rating
from services.metrics_service import get_readed_books_between_dates
from schemas.statistics_schema import parse_date_range
from utils.logger import logger


books_bp = Blueprint("books", __name__, url_prefix="/books")

# Obtener todos los libros y su escritor
@books_bp.route("/", methods=["GET"])
def get_books():
    logger.info("GET /books/")

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
    logger.info("GET /books/ratings")

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

# Libros finalizados en un rango de fechas concreto


@books_bp.route("/readed-books-specific-date", methods=["GET"])
def get_readed_books_in_specific_date():
    logger.info("GET /readed-books-specific-date")
    start_date, end_date = parse_date_range(request.args)
    result = get_readed_books_between_dates(start_date, end_date)
    return jsonify(result)


# Libros más leídos


@books_bp.route("/most-read-books", methods=["GET"])
def get_most_read_books():
    logger.info("GET /statistics/most-read-books")
    rows = fetch_most_read_books()

    books = [
        {
            "book_id": row[0],
            "book_title": row[1],
            "author": row[2],
            "times_read": row[3],
        }
        for row in rows
    ]

    return jsonify(books)
