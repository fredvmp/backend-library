import psycopg2
import os
from dotenv import load_dotenv
from utils.logger import logger


load_dotenv()


def get_connection():

    logger.info("Opening database connection")

    try:
        # Conexión PostgreSQL
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            sslmode="require"
        )
        logger.info("Database connection opened successfully")
        return conn
    except Exception as e:
        logger.error(f"Database connection failed: {e}")

