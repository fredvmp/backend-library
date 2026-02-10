from flask import Flask
from db.connection import get_connection
from routes.books import books_bp
from routes.statistics import statistics_bp
from utils.error_handler import register_error_handlers



def create_app():
    app = Flask(__name__)

    app.register_blueprint(books_bp)
    app.register_blueprint(statistics_bp)
    
    register_error_handlers(app)

    return app


"""
@app.route("/health")
def health():
    # Endpoint conexión db
    try:
        conn = get_connection()
        conn.close()
        return {"status": "ok", "database": "connected"}
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500
"""   
