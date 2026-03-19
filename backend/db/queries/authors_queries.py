from db.connection import get_db_cursor
from utils.logger import logger


def fetch_all_authors():
    logger.info("Executing query: fetch_all_authors")

    query = """
        SELECT id, name
        FROM authors
    """

    with get_db_cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()
