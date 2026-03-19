import pandas as pd
from db.queries.books_queries import fetch_all_books_with_author
from db.queries.books_queries import fetch_books_with_author_country
from db.queries.user_activity_queries import fetch_finished_books_dates


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
