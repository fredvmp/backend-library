from db.connection import get_connection
from utils.logger import logger


def fetch_books():

    conn = get_connection()
    cur = conn.cursor()
    logger.info("Executing query: fetch_books")

    query = """
        SELECT
            b.id,
            b.title,
            a.name AS author
        FROM books b
        JOIN authors a ON b.author_id = a.id
        ORDER BY b.id;
    """

    cur.execute(query)
    rows = cur.fetchall()

    cur.close()
    logger.info("Cursor closed")
    conn.close()
    logger.info("Database connection closed")

    return rows


def fetch_books_with_rating():

    conn = get_connection()
    cur = conn.cursor()
    logger.info("Executing query: fetch_books_with_rating")


    query = """
        SELECT
            b.id,
            b.title,
            a.name AS author,
            ROUND(AVG(r.score), 2) AS average_rating,
            COUNT(r.score) AS total_ratings
        FROM books b
        JOIN authors a ON b.author_id = a.id
        JOIN ratings r ON r.book_id = b.id
        GROUP BY b.id, b.title, a.name
        ORDER BY average_rating DESC;
    """

    cur.execute(query)
    rows = cur.fetchall()

    cur.close()
    logger.info("Cursor closed")
    conn.close()
    logger.info("Database connection closed")

    return rows
