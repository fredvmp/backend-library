from datetime import date, datetime
from db.queries.statistics_queries import fetch_readed_books_in_specific_date


def get_readed_books_between_dates(start_date, end_date):
    rows = fetch_readed_books_in_specific_date(start_date, end_date)

    books = []
    for row in rows:
        books.append({
            "book_id": row[0],
            "book_title": row[1],
            "author": row[2],
            "genres": row[3],
            "ending_date": row[4].isoformat()
        })

    return {
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        "results": books
    }
