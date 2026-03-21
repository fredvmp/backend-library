from flask import jsonify
from utils.errors import APIError, ValidationError
from werkzeug.exceptions import NotFound, MethodNotAllowed
import psycopg2
from utils.logger import logger


def register_error_handlers(app):

    # Errores de API
    @app.errorhandler(APIError)
    def handle_api_error(error):
        logger.warning(f"API Error: {error.message} (Status: {error.status_code})")
        return jsonify({"error": error.message}), error.status_code

    # Errores de la Base de Datos (psycopg2)
    @app.errorhandler(psycopg2.Error)
    def handle_db_error(error):
        logger.error(f"DATABASE ERROR: {getattr(error, 'pgerror', error)}") 
        logger.error(f"Error code: {getattr(error, 'pgcode', 'Unknown')}")
        return jsonify({"error": "Service temporarily unavailable due to database error"}), 500
    
    # Errores de Flask (405)
    @app.errorhandler(NotFound)
    def handle_404_error(e):
        return jsonify({"error": "Resource not found"}), 404
    
    # Errores de Rutas (404)
    @app.errorhandler(MethodNotAllowed)
    def handle_405_error(e):
        return jsonify({"error": "Method not allowed"}), 405
    
    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        return jsonify({"error": "Internal server error"}), 500

    @app.errorhandler(ValidationError)
    def handle_validation_error(e):
        return {"error": e.message}, e.status_code
    
    # Otros errores
    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        logger.error(f"UNEXPECTED ERROR: {error}", exc_info=True) 
        return jsonify({"error": "Internal server error"}), 500
    

    
    