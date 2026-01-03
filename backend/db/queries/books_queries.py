from db.connection import get_connection


def fetch_books():

    conn = get_connection()
    cur = conn.cursor()

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
    conn.close()

    return rows


def fetch_books_with_rating():

    conn = get_connection()
    cur = conn.cursor()

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
    conn.close()

    return rows
