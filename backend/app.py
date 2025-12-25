from flask import Flask
from db.connection import get_connection

app = Flask(__name__)

@app.route("/")
def health_check():
    # Endpoint conexión db
    try:
        conn = get_connection()
        conn.close()
        return {"status": "ok", "database": "connected"}
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500


if __name__ == "__main__":
    app.run(debug=True)
