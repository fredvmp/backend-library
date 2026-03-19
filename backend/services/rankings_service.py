import pandas as pd
from db.queries.users_queries import fetch_all_users
from db.queries.user_activity_queries import fetch_all_ratings
from db.queries.books_queries import fetch_all_books, fetch_all_genres
from db.queries.authors_queries import fetch_all_authors


def get_negative_ratings_ranking():

    rows_users = []
    rows_ratings = []

    rows_users = fetch_all_users()
    rows_ratings = fetch_all_ratings()

    df_users = pd.DataFrame(rows_users, columns=["id_user", "username"])
    df_ratings = pd.DataFrame(rows_ratings, columns=[
                              "id_user", "book_id", "score"])

    #                            left_on="id_user", right_on="id_user"  (tabla users y rating respectivamente)
    df_merged = pd.merge(df_users, df_ratings, how="inner", on="id_user")
    ranking = df_merged.groupby("username").agg(
        avg_score=("score", "mean"),
        total_ratings=("score", "count")
    )

    ranking = ranking[ranking["total_ratings"] > 1]

    ranking = ranking.sort_values("avg_score", ascending=True)

    return ranking.round(2).reset_index().to_dict(orient="records")


def get_cult_classics():

    rows_ratings = fetch_all_ratings()
    rows_books = fetch_all_books()
    rows_authors = fetch_all_authors()

    df_ratings = pd.DataFrame(rows_ratings, columns=[
                              "user_id", "book_id", "score"])
    df_books = pd.DataFrame(rows_books, columns=[
                            "book_id", "title_book", "author_id", "genre_id"])
    df_authors = pd.DataFrame(rows_authors, columns=[
                              "author_id", "author_name"])

    df_final = pd.merge(df_books, df_authors, on="author_id", how="inner").merge(
        df_ratings, on="book_id", how="inner")
    summary = df_final.groupby(["book_id", "title_book"]).agg(
        avg_score=("score", "mean"),
        total_ratings=("score", "count"),
        author_name=("author_name", "first")
    )

    summary = summary[summary["total_ratings"] > 1]
    summary = summary.sort_values("avg_score", ascending=False)

    return summary.round(2).reset_index().to_dict(orient="records")


def get_genre_users_ranking(genre_name: str):

    rows_ratings = fetch_all_ratings()
    rows_books = fetch_all_books()
    rows_users = fetch_all_users()
    rows_genres = fetch_all_genres()

    df_ratings = pd.DataFrame(rows_ratings, columns=[
                              "user_id", "book_id", "score"])
    df_books = pd.DataFrame(rows_books, columns=[
                            "book_id", "book_title", "book_author", "book_genre"])
    df_users = pd.DataFrame(rows_users, columns=["user_id", "username"])
    df_genres = pd.DataFrame(rows_genres, columns=["genre_id", "genre_name"])

    # Limpiar datos
    # genre_name = genre_name.strip().capitalize()
    # df_genres["genre_name"] = df_genres["genre_name"].str.strip().str.capitalize()

    df_books["book_genre"] = pd.to_numeric(
        df_books["book_genre"], errors='coerce')  # fuerza el cambio
    df_genres["genre_id"] = pd.to_numeric(
        df_genres["genre_id"], errors='coerce')

    df_merged = pd.merge(df_books, df_genres, left_on="book_genre", right_on="genre_id", how="inner").merge(
        df_ratings, on="book_id", how="inner").merge(df_users, on="user_id", how="inner")
    df_merged = df_merged[["username", "genre_name",
                           "book_id", "book_title", "score"]]

    # Filtrar por género
    df_merged = df_merged[df_merged["genre_name"] == genre_name]

    summary = df_merged.groupby(["username", "genre_name"]).agg(
        readed_books=("book_id", "count"),
        avg_score=("score", "mean"),
    )

    summary = summary[summary["readed_books"] > 1]
    summary = summary.sort_values("avg_score", ascending=False)

    return summary.round(2).reset_index().to_dict(orient="records")
