from flask import Flask
from db.connection import get_connection
from routes.books import books_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(books_bp)

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

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
