from db.connection import get_connection
from utils.logger import logger
from flask import jsonify


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


# Statistic with pandas
def fetch_all_books_with_author():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT a.name
        FROM books b
        JOIN authors a ON b.author_id = a.id
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


def fetch_books_with_author_country():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT a.country
        FROM books b
        JOIN authors a ON b.author_id = a.id
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


def fetch_finished_books_dates():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT status_date
        FROM reading_status_history
        WHERE status = 'FINISHED'
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


def fetch_reading_summary():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT book_id, user_id, status_date
        FROM reading_status_history
        WHERE status = 'FINISHED'
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


def fetch_genre_reading_velocity():

    try:

        conn = get_connection()
        cursor = conn.cursor()
        logger.info("Executing query: fetch_genre_reading_velocity")

        query = """
            SELECT DISTINCT ON (u.username, be.pages, g.name) 
                u.username, be.pages, g.name, rsh_start.status_date, rsh_end.status_date
            FROM genres g
            JOIN book_genres bg 
                ON g.id = bg.genre_id
            JOIN books b 
                ON bg.book_id = b.id
            JOIN reading_status_history rsh_start 
                ON b.id = rsh_start.book_id
            JOIN reading_status_history rsh_end 
                ON rsh_start.book_id = rsh_end.book_id
                AND rsh_start.user_id = rsh_end.user_id
                AND rsh_end.status_date > rsh_start.status_date
            JOIN users u 
                ON rsh_end.user_id  = u.id
            JOIN book_editions be
                ON b.id = be.book_id
            WHERE rsh_start.status = 'READING' 
                AND rsh_end.status = 'FINISHED'
            ORDER BY u.username, be.pages, g.name, rsh_end.status_date DESC
        """

        cursor.execute(query)
        rows = cursor.fetchall()

    except Exception as e:
        logger.error(f"Error getting data: {e}")

    finally:

        cursor.close()
        conn.close()

    return rows


def fetch_all_users():

    try:

        conn = get_connection()
        cursor = conn.cursor()
        logger.info("Executing query: fetch_all_users")

        query = """
            SELECT id, username
            FROM users
        """

        cursor.execute(query)
        rows = cursor.fetchall()

    except Exception as e:
        logger.error(f"Error getting data: {e}")

    finally:

        cursor.close()
        conn.close()

    return rows

def fetch_all_ratings():

    try:

        conn = get_connection()
        cursor = conn.cursor()
        logger.info("Executing query: fetch_all_ratings")

        query = """
            SELECT user_id, book_id, score
            FROM ratings
        """

        cursor.execute(query)
        rows = cursor.fetchall()

    except Exception as e:
        logger.error(f"Error getting data: {e}")

    finally:

        cursor.close()
        conn.close()

    return rows


def fetch_all_books():

    try:

        conn = get_connection()
        cursor = conn.cursor()
        logger.info("Executing query: fetch_all_books")

        query = """
            SELECT id, title, author_id
            FROM books
        """

        cursor.execute(query)
        rows = cursor.fetchall()

    except Exception as e:
        logger.error(f"Error getting data: {e}")

    finally:

        cursor.close()
        conn.close()

    return rows

def fetch_all_authors():

    try:

        conn = get_connection()
        cursor = conn.cursor()
        logger.info("Executing query: fetch_all_authors")

        query = """
            SELECT id, name
            FROM authors
        """

        cursor.execute(query)
        rows = cursor.fetchall()

    except Exception as e:
        logger.error(f"Error getting data: {e}")

    finally:

        cursor.close()
        conn.close()

    return rows

