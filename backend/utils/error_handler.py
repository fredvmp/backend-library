from flask import jsonify
from utils.errors import APIError, ValidationError
import psycopg2

def register_error_handlers(app):

    @app.errorhandler(APIError)
    def handle_api_error(error):
        return jsonify({"error": error.message}), error.status_code

    @app.errorhandler(psycopg2.Error)
    def handle_db_error(error):
        return jsonify({"error": "Database error"}), 500

    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        return jsonify({"error": "Internal server error"}), 500

    @app.errorhandler(ValidationError)
    def handle_validation_error(e):
        return {"error": e.message}, e.status_code