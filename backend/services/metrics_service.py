import pandas as pd
from utils.logger import logger
from db.queries.books_queries import fetch_readed_books_in_specific_date
from db.queries.user_activity_queries import fetch_reading_summary
from db.queries.analytics_queries import fetch_genre_reading_velocity
from db.queries.user_activity_queries import fetch_all_reading_status_history
from db.queries.books_queries import fetch_all_books, fetch_all_genres, fetch_all_book_editions


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
    df["year_month"] = df["status_date"].dt.to_period("M")

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


""" Ranking de géneros según la media de páginas leídas 
    por día por los usuarios en cada género """


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
    ).assign(avg_pages=lambda x: x.avg_pages.round(0).astype("Int64")).reset_index().sort_values(
        "avg_pages", ascending=False).to_dict(orient="records")

    return data


def get_genre_dropout_rate():

    rows_books = fetch_all_books()
    rows_genres = fetch_all_genres()
    rows_rsh = fetch_all_reading_status_history()

    df_books = pd.DataFrame(rows_books, columns=[
                            "book_id", "book_title", "book_author", "book_genre_id"])
    df_genres = pd.DataFrame(rows_genres, columns=["genre_id", "genre_name"])
    df_rsh = pd.DataFrame(rows_rsh, columns=[
                          "rsh_id", "rsh_status", "rsh_status_date", "rsh_user_id", "rsh_book_id"])

    """
    df_rsh["rsh_book_id"] = df_rsh["rsh_book_id"].astype("Int64")
    df_books["book_id"] = df_books["book_id"].astype("Int64")
    df_books["book_genre_id"] = df_books["book_genre_id"].astype("Int64")
    df_genres["genre_id"] = df_genres["genre_id"].astype("Int64")
    """

    df_merged = pd.merge(df_rsh, df_books, how="inner", left_on="rsh_book_id", right_on="book_id").merge(
        df_genres, how="inner", left_on="book_genre_id", right_on="genre_id")
    df_merged = df_merged[["book_id", "genre_name", "genre_id",
                           "rsh_status", "rsh_status_date"]]

    """
    if df_merged.empty:
        return []
    """

    df_merged["rsh_status_date"] = pd.to_datetime(df_merged["rsh_status_date"])
    time_90_days = pd.Timestamp.now() - pd.Timedelta(days=90)
    df_merged["rsh_status"] = df_merged["rsh_status"].str.strip().str.capitalize()
    df_merged["genre_name"] = df_merged["genre_name"].str.strip()

    df_merged.loc[df_merged["rsh_status"] ==
                  "Abandoned", "reading_type"] = "Abandoned"
    df_merged.loc[
        (df_merged["rsh_status"] == "Reading") &
        (df_merged["rsh_status_date"] < time_90_days),
        "reading_type"] = "Abandoned"
    df_merged.loc[
        (df_merged["rsh_status"] == "Reading") &
        (df_merged["rsh_status_date"] > time_90_days),
        "reading_type"] = "Reading"
    df_merged.loc[df_merged["rsh_status"] ==
                  "Finished", "reading_type"] = "Finished"

    result = df_merged.groupby("genre_name").agg(
        abandoned_count=(
            "reading_type", lambda x: (x == "Abandoned").sum()),
        total_records=("reading_type", "count")

    ).assign(dropout_rate=lambda x: (x.abandoned_count / x.total_records) * 100).round(2).reset_index(
    ).sort_values("dropout_rate", ascending=False).to_dict(orient="records")

    return result


def get_genre_format_popularity():

    rows_books = fetch_all_books()
    rows_genres = fetch_all_genres()
    rows_book_editions = fetch_all_book_editions()

    df_books = pd.DataFrame(rows_books, columns=[
                            "book_id", "book_title", "book_author", "book_genre_id"])
    df_genres = pd.DataFrame(rows_genres, columns=["genre_id", "genre_name"])
    df_book_editions = pd.DataFrame(rows_book_editions, columns=[
                                    "book_edition_id", "isbn", "format", "book_id"])

    df_merged = pd.merge(df_books, df_genres, how="inner", left_on="book_genre_id",
                         right_on="genre_id").merge(df_book_editions, how="inner", on="book_id")

    pivot_popularity = (
        df_merged
        .dropna(subset=["isbn"])
        .loc[lambda x: (x["isbn"].notna()) & (x["isbn"] != "")]
        .pivot_table(
            index="genre_name",
            columns="format",
            values="book_edition_id",
            aggfunc="count",
            fill_value=0,
            margins=True
        )
    )

    return pivot_popularity
