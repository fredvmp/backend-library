import pandas as pd
from db.queries.books_queries import fetch_readed_books_in_specific_date
from db.queries.user_activity_queries import fetch_reading_summary
from db.queries.analytics_queries import fetch_genre_reading_velocity
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


def get_reading_summary():

    rows = fetch_reading_summary()

    df = pd.DataFrame(rows, columns=["book_id", "user_id", "status_date"])

    df["status_date"] = pd.to_datetime(df["status_date"])
    # df["year"] = df["status_date"].dt.year
    # df["month"] = df["status_date"].dt.month
    df["year_month"] = df["status_date"].dt.to_period('M')

    summary = df.groupby("year_month").agg(  # agregar funciones
        unique_users=("user_id", "nunique"),
        unique_books=("book_id", "nunique"),
        books_finished=("book_id", "count"),

        # Permite crear columnas nuevas en base a las creadas en el .agg
    ).assign(avg_books_per_user=lambda x: (x.books_finished / x.unique_users).round(2))

    # Pasar las fechas a texto
    summary.index = summary.index.astype(str)
    # Reiniciar índice y convertir la tabla en una lista de diccionarios
    return summary.reset_index().to_dict(orient="records")


''' Ranking de géneros según la media de páginas leídas 
    por día por los usuarios en cada género '''


def get_genre_reading_velocity():

    rows = fetch_genre_reading_velocity()

    df = pd.DataFrame(
        rows, columns=["user", "book_pages", "genre_name", "date_start", "date_end"])

    df = df.dropna(subset=["book_pages"])

    df["date_start"] = pd.to_datetime(df["date_start"])
    df["date_end"] = pd.to_datetime(df["date_end"])
    df["reading_days"] = (df["date_end"] - df["date_start"]).dt.days
    df["reading_days"] = df["reading_days"].clip(lower=1)

    df["pages_per_day"] = df["book_pages"] / df["reading_days"]

    data = df.groupby("genre_name").agg(
        avg_pages=("pages_per_day", "mean"),
        users=("user", "nunique")
    ).assign(avg_pages=lambda x: x.avg_pages.round(0).astype('Int64')).reset_index().sort_values(
        "avg_pages", ascending=False).to_dict(orient="records")

    return data
