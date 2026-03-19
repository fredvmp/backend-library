from flask import Flask
from routes.books_bp import books_bp
from routes.metrics_bp import metrics_bp
from routes.rankings_bp import rankings_bp
from utils.error_handler import register_error_handlers


def create_app():
    app = Flask(__name__)

    app.json.ensure_ascii = False

    app.register_blueprint(books_bp)
    app.register_blueprint(metrics_bp)
    app.register_blueprint(rankings_bp)

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
