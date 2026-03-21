from flask import Blueprint, jsonify
import psycopg2
from services.rankings_service import get_negative_ratings_ranking
from services.rankings_service import get_cult_classics
from services.rankings_service import get_genre_users_ranking
from utils.logger import logger


rankings_bp = Blueprint("rankings", __name__, url_prefix="/rankings")


@rankings_bp.route("/negative-ratings-ranking", methods=["GET"])
def negative_ratings_ranking():
    result = get_negative_ratings_ranking()
    if not result:
        return jsonify({"message": "No data available"}), 200
    return jsonify(result), 200


@rankings_bp.route("cult-classics", methods=["GET"])
def cult_classics():
    result = get_cult_classics()
    if not result:
        return jsonify({"message": "No data available"}), 200
    return jsonify(result), 200


@rankings_bp.route("genre-users-ranking/<string:genre_name>", methods=["GET"])
def genre_users_ranking(genre_name):
    result = get_genre_users_ranking(genre_name)
    if not result:
        return jsonify({"message": "No data available"}), 200
    return jsonify(result), 200
