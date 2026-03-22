from db.connection import get_db_cursor
from utils.logger import logger


def fetch_all_users():
    logger.info("Executing query: fetch_all_users")

    query = """
        SELECT id, username 
        FROM users
    """

    with get_db_cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()


