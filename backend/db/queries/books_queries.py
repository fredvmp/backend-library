from db.connection import get_db_cursor
from utils.logger import logger


def fetch_books():
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

    with get_db_cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()


def fetch_books_with_rating():
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

    with get_db_cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()


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


def fetch_all_books():
    logger.info("Executing query: fetch_all_books")

    query = """
        SELECT id, title, author_id, genre_id
        FROM books
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


def fetch_all_book_editions():
    logger.info("Executing query: fetch_all_book_editions")

    query = """
        SELECT id, isbn, format, book_id, pages
        FROM book_editions
    """

    with get_db_cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def fetch_books_detailed():
    logger.info("Executing query: fetch_books_detailed")

    query = """
        SELECT b.id AS book_id, 
            b.title, 
            a.name AS author_name,
            g.name AS genre_name,
            be.pages, 
            be.format, 
            be.isbn
        FROM books b
        LEFT JOIN book_genres bg ON b.id = bg.book_id
        LEFT JOIN genres g ON g.id = bg.genre_id
        LEFT JOIN book_editions be ON be.book_id = b.id
        LEFT JOIN authors a ON a.id = b.author_id
    """

    with get_db_cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()
