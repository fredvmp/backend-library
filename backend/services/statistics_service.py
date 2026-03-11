from datetime import date, datetime
import pandas as pd
from db.queries.statistics_queries import fetch_readed_books_in_specific_date
from db.queries.statistics_queries import fetch_all_books_with_author
from db.queries.statistics_queries import fetch_books_with_author_country
from db.queries.statistics_queries import fetch_finished_books_dates

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

    # Dataframe llamado author
    df = pd.DataFrame(rows, columns=["author"])

    # Agrupar por autor
    author_counts = df["author"].value_counts()

    # Pasar tabla a un diccionario
    return author_counts.to_dict()


def get_books_per_country():

    rows = fetch_books_with_author_country()

    # Dataframe llamado country
    df = pd.DataFrame(rows, columns=["country"])

    # Agrupar
    result = df["country"].value_counts()

    # Pasar tabla a un diccionario
    return result.to_dict()


def get_books_finished_by_year():

    rows = fetch_finished_books_dates()

    df = pd.DataFrame(rows, columns=["status_date"])

    #                   convierte texto en fechas
    df["status_date"] = pd.to_datetime(df["status_date"])

    #                       extraer el año de status_date
    df["year"] = df["status_date"].dt.year


    #                   Ordenar por frecuencia
    result = df["year"].value_counts().sort_index()

    return result.to_dict()
