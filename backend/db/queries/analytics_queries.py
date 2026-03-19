from db.connection import get_db_cursor
from utils.logger import logger


def fetch_genre_reading_velocity():
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

    with get_db_cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()
