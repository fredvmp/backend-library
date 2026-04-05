from flask import Blueprint, jsonify, request, Response
import psycopg2
from services.metrics_service import get_reading_summary, get_genre_reading_velocity, get_genre_dropout_rate, get_genre_format_popularity, get_pivot_user_reading_velocity, get_pbi_user_reading_velocity, get_user_reading_metrics, get_book_quality_metrics
from services.books_service import get_books_per_author, get_books_per_country, get_books_finished_by_year
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
    result = get_books_finished_by_year()
    return jsonify(result), 200


@metrics_bp.route("/monthly-reading-summary", methods=["GET"])
def monthly_reading_summary():
    result = get_reading_summary()
    return jsonify(result), 200


@metrics_bp.route("/genre-reading-velocity", methods=["GET"])
def genre_reading_velocity():
    result = get_genre_reading_velocity()
    if not result:
        return jsonify({"message": "No data available"}), 200
    return jsonify(result), 200


@metrics_bp.route("/genre-dropout-rate", methods=["GET"])
def genre_dropout_rate():
    result = get_genre_dropout_rate()
    if not result:
        return jsonify({"message": "No data available"}), 200
    return jsonify(result), 200


@metrics_bp.route("/genre-format-popularity", methods=["GET"])
def genre_format_popularity():
    result = get_genre_format_popularity()
    if result.empty:
        return jsonify({"message": "No data available"}), 200
    # return jsonify(result.to_dict(orient="index")), 200
    return result.to_html(classes="table table-striped"), 200


@metrics_bp.route("/pivot-user-reading-velocity", methods=["GET"])
def pivot_user_reading_velocity():
    result = get_pivot_user_reading_velocity()
    if result.empty:
        return jsonify({"message": "No data available"}), 200
    return result.to_html(classes="table table-striped"), 200


@metrics_bp.route("/pbi-user-reading-velocity", methods=["GET"])
def pbi_user_reading_velocity():
    result = get_pbi_user_reading_velocity()
    if result.empty:
        return jsonify([]), 200
    data = result.to_dict(orient="records")
    return jsonify(data), 200


@metrics_bp.route("/user-reading-metrics", methods=["GET"])
def user_reading_metrics():
    result = get_user_reading_metrics()
    if result.empty:
        return jsonify([]), 200
    data = result.to_dict(orient="records")
    return jsonify(data), 200

@metrics_bp.route("/book-quality-metrics", methods=["GET"])
def book_quality_metrics():
    result = get_book_quality_metrics()
    if result.empty:
        return jsonify([]), 200
    data = result.to_dict(orient="records")
    return jsonify(data), 200