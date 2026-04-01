import pandas as pd
import numpy as np
import json
from utils.logger import logger
from db.queries.books_queries import fetch_readed_books_in_specific_date
from db.queries.user_activity_queries import fetch_reading_summary
from db.queries.users_queries import fetch_all_users
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
                                    "book_edition_id", "isbn", "format", "book_id", "pages"])

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


def get_pivot_user_reading_velocity():

    rows_books = fetch_all_books()
    rows_rsh = fetch_all_reading_status_history()
    rows_users = fetch_all_users()

    df_books = pd.DataFrame(rows_books, columns=[
                            "book_id", "book_title", "book_author", "book_genre_id"])
    df_rsh = pd.DataFrame(rows_rsh, columns=[
                          "rsh_id", "rsh_status", "rsh_status_date", "rsh_user_id", "rsh_book_id"])
    df_users = pd.DataFrame(rows_users, columns=["user_id", "username"])

    df_merged = pd.merge(df_books, df_rsh, how="inner", left_on="book_id", right_on="rsh_book_id").merge(
        df_users, left_on="rsh_user_id", right_on="user_id")

    df_merged = df_merged[["book_id", "rsh_status",
                           "rsh_status_date", "username"]]

    df_merged["rsh_status_date"] = pd.to_datetime(df_merged["rsh_status_date"])
    df_merged["year_month"] = df_merged["rsh_status_date"].dt.to_period(
        "M")  # 2026-03

    pivot_velocity = (
        df_merged
        .loc[df_merged["rsh_status"].isin(["FINISHED", "READING", "ABANDONED"])]
        .groupby("username").filter(lambda x: x["rsh_status"].count() >= 3)
        .pivot_table(
            index=["year_month", "username"],
            columns="rsh_status",
            values="book_id",
            aggfunc="nunique",
            fill_value=0
        )
    )

    return pivot_velocity


def get_pbi_user_reading_velocity():

    rows_books = fetch_all_books()
    rows_rsh = fetch_all_reading_status_history()
    rows_users = fetch_all_users()

    df_books = pd.DataFrame(rows_books, columns=[
                            "book_id", "book_title", "book_author", "book_genre_id"])
    df_rsh = pd.DataFrame(rows_rsh, columns=[
                          "rsh_id", "rsh_status", "rsh_status_date", "rsh_user_id", "rsh_book_id"])
    df_users = pd.DataFrame(rows_users, columns=["user_id", "username"])

    df_merged = pd.merge(df_books, df_rsh, how="inner", left_on="book_id", right_on="rsh_book_id").merge(
        df_users, left_on="rsh_user_id", right_on="user_id")

    df_merged = df_merged[["book_id", "rsh_status",
                           "rsh_status_date", "username"]]

    df_merged["rsh_status_date"] = pd.to_datetime(df_merged["rsh_status_date"])
    # df_merged["year_month"] = df_merged["rsh_status_date"].dt.to_period("M")  # 2026-03

    result = (
        df_merged
        .loc[df_merged["rsh_status"].isin(["FINISHED", "READING", "ABANDONED"])]
        .groupby("username").filter(lambda x: x["rsh_status"].count() >= 3)
    ).copy()

    result["rsh_status_date"] = result["rsh_status_date"].dt.strftime(
        '%Y-%m-%d')

    return result


def get_user_reading_metrics():
    rows_rsh = fetch_all_reading_status_history()
    rows_users = fetch_all_users()
    rows_books = fetch_all_books()
    rows_editions = fetch_all_book_editions()

    df_rsh = pd.DataFrame(rows_rsh, columns=["rsh_id", "rsh_status", "rsh_status_date", "user_id", "book_id"])
    df_users = pd.DataFrame(rows_users, columns=["user_id", "username"])
    df_books = pd.DataFrame(rows_books, columns=["book_id", "title", "author", "genre_id"])
    df_editions = pd.DataFrame(rows_editions, columns=["edition_id", "isbn", "format", "book_id", "pages"])

    df_merged = df_rsh.merge(df_users, on="user_id").merge(df_books, on="book_id").merge(df_editions, on="book_id")

    df_merged["rsh_status_date"] = pd.to_datetime(df_merged["rsh_status_date"])
    df_merged = df_merged.sort_values(["username", "book_id", "rsh_status_date"])

    df_merged["prev_date"] = df_merged.groupby(["username", "book_id"])["rsh_status_date"].shift(1)
    df_merged["prev_status"] = df_merged.groupby(["username", "book_id"])["rsh_status"].shift(1)

    df_final = df_merged[(df_merged["rsh_status"] == "FINISHED") & (df_merged["prev_status"] == "READING")].copy()

    if df_final.empty:
        return df_final

    df_final["days_taken"] = (df_final["rsh_status_date"] - df_final["prev_date"]).dt.days
    df_final["reading_speed"] = df_final["pages"] / df_final["days_taken"].replace(0, 1)

    first_ever = df_merged.groupby("username")["rsh_status_date"].transform("min")
    df_final["user_seniority_days"] = (pd.Timestamp.now() - first_ever).dt.days

    columns_to_send = ["username", "title", "pages", "days_taken", "reading_speed", "user_seniority_days", "format"]
    df_output = df_final[columns_to_send].copy()

    df_output = df_output.replace([np.inf, -np.inf], 0).fillna(0)
    df_output["reading_speed"] = df_output["reading_speed"].round(2)

    df_output["days_taken"] = df_output["days_taken"].astype("Int64")
    df_output["user_seniority_days"] = df_output["user_seniority_days"].astype("Int64")
    df_output["pages"] = df_output["pages"].astype("Int64")

    return df_output