from db.connection import get_connection
from utils.logger import logger


def fetch_most_read_books():

    conn = get_connection()
    cur = conn.cursor()
    logger.info("Executing query: fetch_most_read_books")

    try:

        query = """
            SELECT 
                b.id, 
                b.title, 
                a.name AS author, 
                COUNT(DISTINCT rsh.user_id) AS times_read
            FROM books b
            JOIN reading_status_history rsh ON b.id = rsh.book_id
            JOIN authors a ON b.author_id = a.id
            WHERE rsh.status = 'FINISHED'
            GROUP BY b.id, b.title, a.name
            ORDER BY times_read DESC;
        """

        cur.execute(query)
        return cur.fetchall()

    finally:
        if cur:
            cur.close()
            logger.info("Cursor closed")
        if conn:
            conn.close()
            logger.info("Database connection closed")


def fetch_readed_books_in_specific_date(start_date, end_date):

    conn = None
    cur = None
    logger.info("Executing query: fetch_readed_books_in_specific_date")

    try:
        conn = get_connection()
        cur = conn.cursor()

        query = """
            SELECT 
                b.id,
                b.title,
                a.name AS author,
                ARRAY_AGG(DISTINCT g.name) AS genres,
                rsh.status_date AS ending_date
            FROM books b
            JOIN book_genres bg ON b.id = bg.book_id
            JOIN genres g ON g.id = bg.genre_id
            JOIN authors a ON b.author_id = a.id
            JOIN reading_status_history rsh ON b.id = rsh.book_id
            WHERE rsh.status = 'FINISHED'
                AND rsh.status_date BETWEEN %s AND %s
            GROUP BY b.id, b.title, a.name, rsh.status_date
            ORDER BY rsh.status_date DESC;
        """

        cur.execute(query, (start_date, end_date))
        return cur.fetchall()

    finally:
        if cur:
            cur.close()
            logger.info("Cursor closed")
        if conn:
            conn.close()
            logger.info("Database connection closed")
