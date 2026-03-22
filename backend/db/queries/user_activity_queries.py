from db.connection import get_db_cursor
from utils.logger import logger


def fetch_all_ratings():
    logger.info("Executing query: fetch_all_ratings")

    query = """
        SELECT user_id, book_id, score
        FROM ratings
    """

    with get_db_cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()


def fetch_reading_summary():
    logger.info("Executing query: fetch_reading_summary")

    query = """
        SELECT book_id, user_id, status_date
        FROM reading_status_history
        WHERE status = 'FINISHED'
    """

    with get_db_cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()

def fetch_finished_books_dates():
    logger.info("Executing query: fetch_finished_books_dates")

    query = """
        SELECT status_date
        FROM reading_status_history
        WHERE status = 'FINISHED'
    """

    with get_db_cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()
    

def fetch_all_reading_status_history():
    logger.info("Executing query: fetch_all_reading_status_history")

    query = """
        SELECT *
        FROM reading_status_history
    """

    with get_db_cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()