from datetime import date, datetime
from db.queries.statistics_queries import fetch_readed_books_in_specific_date


def get_readed_books_between_dates(start_date_str, end_date_str):

    if not start_date_str:
        raise ValueError("start date is required (yyyy-mm-dd)")

    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
        end_date = (
            datetime.strptime(end_date_str, "%Y-%m-%d").date()
            if end_date_str
            else date.today()
        )
    except ValueError:
        raise ValueError("Invalid date format. Use yyyy-mm-dd")

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
