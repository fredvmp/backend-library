from flask import Blueprint, jsonify, request
import psycopg2
from db.queries.statistics_queries import fetch_most_read_books
from services.statistics_service import get_readed_books_between_dates
from schemas.statistics_schema import parse_date_range

statistics_bp = Blueprint("statistics", __name__, url_prefix="/statistics")


# Libros más leídos
@statistics_bp.route("/most-read-books", methods=["GET"])
def get_most_read_books():
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


# Libros finalizados en un rango de fechas concreto
@statistics_bp.route("/readed-books-specific-date", methods=["GET"])
def get_readed_books_in_specific_date():
    start_date, end_date = parse_date_range(request.args)
    result = get_readed_books_between_dates(start_date, end_date)
    return jsonify(result)
