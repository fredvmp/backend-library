from flask import Blueprint, jsonify
import psycopg2
from services.rankings_service import get_negative_ratings_ranking
from services.rankings_service import get_cult_classics
from services.rankings_service import get_genre_users_ranking
from utils.logger import logger


rankings_bp = Blueprint("rankings", __name__, url_prefix="/rankings")


@rankings_bp.route("/negative-ratings-ranking", methods=["GET"])
def negative_ratings_ranking():
    try:
        result = get_negative_ratings_ranking()
        if not result:
            return jsonify({"message": "No data available"}), 200
        return jsonify(result), 200

    except psycopg2.DatabaseError as e:
        logger.error(f"DB Error: {e}")
        return jsonify({"error": "Service temporarily unavailable"}), 503

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({"error": "Internal server error"}), 500


@rankings_bp.route("cult-classics", methods=["GET"])
def cult_classics():
    try:
        result = get_cult_classics()
        if not result:
            return jsonify({"message": "No data available"}), 200
        return jsonify(result), 200

    except psycopg2.DatabaseError as e:
        logger.error(f"DB Error: {e}")
        return jsonify({"error": "Service temporarily unavailable"}), 503

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({"error": "Internal server error"}), 500


@rankings_bp.route("genre-users-ranking/<string:genre_name>", methods=["GET"])
def genre_users_ranking(genre_name):

    try:
        result = get_genre_users_ranking(genre_name)
        if not result:
            return jsonify({"message": "No data available"}), 200
        return jsonify(result), 200

    except psycopg2.DatabaseError as e:
        logger.error(f"DB Error: {e}")
        return jsonify({"error": "Service temporarily unavailable"}), 503

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({"error": "Internal server error"}), 500
