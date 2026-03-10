from datetime import date, datetime
import pandas as pd
from db.queries.statistics_queries import fetch_readed_books_in_specific_date
from db.queries.statistics_queries import fetch_all_books_with_author
from utils.logger import logger


def get_readed_books_between_dates(start_date, end_date):
    logger.info(f"Fetching books between {start_date} and {end_date}")
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


# Statistic with pandas
def get_books_per_author():
    rows = fetch_all_books_with_author()
    
    # Convertir a DataFrame
    df = pd.DataFrame(rows, columns=["author"])

    # Agrupar por autor
    author_counts = df["author"].value_counts()

    return author_counts.to_dict()
