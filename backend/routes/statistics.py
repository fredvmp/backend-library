from flask import Blueprint, jsonify, request
import psycopg2
from db.queries.statistics_queries import fetch_most_read_books
from services.statistics_service import get_readed_books_between_dates
from schemas.statistics_schema import parse_date_range
from services.statistics_service import get_books_per_author
from services.statistics_service import get_books_per_country
from services.statistics_service import get_books_finished_by_year
from services.statistics_service import get_reading_summary
from services.statistics_service import get_genre_reading_velocity
from utils.logger import logger


statistics_bp = Blueprint("statistics", __name__, url_prefix="/statistics")


# Libros más leídos
@statistics_bp.route("/most-read-books", methods=["GET"])
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


# Libros finalizados en un rango de fechas concreto
@statistics_bp.route("/readed-books-specific-date", methods=["GET"])
def get_readed_books_in_specific_date():
    logger.info("GET /readed-books-specific-date")
    start_date, end_date = parse_date_range(request.args)
    result = get_readed_books_between_dates(start_date, end_date)
    return jsonify(result)


# Statistic with pandas
@statistics_bp.route("/books-per-author", methods=["GET"])
def books_per_author():
    result = get_books_per_author()
    return jsonify(result)

@statistics_bp.route("/books-per-country", methods=["GET"])
def books_per_country():
    data = get_books_per_country()
    return jsonify(data)

@statistics_bp.route("/books-by-year", methods=["GET"])
def books_by_year():

    try:
        result = get_books_finished_by_year()
        return jsonify(result), 200

    except Exception as e:
        logger.error(f"Error getting books by year: {e}")
        return jsonify({"error": "Database error"}), 500


@statistics_bp.route("/monthly-reading-summary", methods=["GET"])
def get_monthly_reading_summary():

    try:
        result = get_reading_summary()
        return jsonify(result), 200

    except Exception as e:
        logger.error(f"Error getting data: {e}")
        return jsonify({"error": "Database error"}), 500



@statistics_bp.route("/genre-reading-velocity", methods=["GET"])
def genre_reading_velocity():

    try:
        result = get_genre_reading_velocity()
        if not result:
            return jsonify({"message": "No data available"}), 200
        return jsonify(result), 200
    
    except psycopg2.DatabaseError as e:
        logger.error(f"DB Error: {e}")
        return jsonify({"error": "Service temporarily unavailable"}), 503
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({"error": "Internal server error"}), 500


