from db.connection import get_connection, get_db_cursor
from utils.logger import logger
from flask import jsonify


def fetch_most_read_books():
    logger.info("Executing query: fetch_most_read_books")

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

    with get_db_cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()


def fetch_readed_books_in_specific_date(start_date, end_date):
    logger.info("Executing query: fetch_readed_books_in_specific_date")

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
    with get_db_cursor() as cursor:
        cursor.execute(query, (start_date, end_date))
        return cursor.fetchall()


def fetch_all_books_with_author():
    logger.info("Executing query: fetch_all_books_with_author")

    query = """
        SELECT a.name
        FROM books b
        JOIN authors a ON b.author_id = a.id
    """

    with get_db_cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()


def fetch_books_with_author_country():
    logger.info("Executing query: fetch_books_with_author_country")

    query = """
        SELECT a.country
        FROM books b
        JOIN authors a ON b.author_id = a.id
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


def fetch_all_users():
    logger.info("Executing query: fetch_all_users")

    query = """
        SELECT id, username 
        FROM users
    """

    with get_db_cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()


def fetch_all_ratings():
    logger.info("Executing query: fetch_all_ratings")

    query = """
        SELECT user_id, book_id, score
        FROM ratings
    """

    with get_db_cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()


def fetch_all_books():
    logger.info("Executing query: fetch_all_books")

    query = """
        SELECT id, title, author_id, genre_id
        FROM books
    """

    with get_db_cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()


def fetch_all_authors():
    logger.info("Executing query: fetch_all_authors")

    query = """
        SELECT id, name
        FROM authors
    """

    with get_db_cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()


def fetch_all_genres():
    logger.info("Executing query: fetch_all_genres")

    query = """
        SELECT id, name
        FROM genres
    """

    with get_db_cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()
