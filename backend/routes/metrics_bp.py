from flask import Blueprint, jsonify, request
import psycopg2
from services.metrics_service import get_reading_summary
from services.metrics_service import get_genre_reading_velocity
from services.books_service import get_books_per_author, get_books_per_country, get_books_finished_by_year
from utils.logger import logger


from utils.logger import logger


metrics_bp = Blueprint("metrics", __name__, url_prefix="/metrics")


@metrics_bp.route("/books-per-author", methods=["GET"])
def books_per_author():
    result = get_books_per_author()
    return jsonify(result)


@metrics_bp.route("/books-per-country", methods=["GET"])
def books_per_country():
    data = get_books_per_country()
    return jsonify(data)


@metrics_bp.route("/books-by-year", methods=["GET"])
def books_by_year():

    try:
        result = get_books_finished_by_year()
        return jsonify(result), 200

    except Exception as e:
        logger.error(f"Error getting books by year: {e}")
        return jsonify({"error": "Database error"}), 500


@metrics_bp.route("/monthly-reading-summary", methods=["GET"])
def get_monthly_reading_summary():

    try:
        result = get_reading_summary()
        return jsonify(result), 200

    except Exception as e:
        logger.error(f"Error getting data: {e}")
        return jsonify({"error": "Database error"}), 500


@metrics_bp.route("/genre-reading-velocity", methods=["GET"])
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
