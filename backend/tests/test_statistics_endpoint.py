from unittest.mock import patch


def test_statistics_endpoint(client):
    fake_response = {
        "start_date": "2024-01-01",
        "end_date": "2024-01-10",
        "results": [
            {
                "book_id": 1,
                "book_title": "Kafka on the Shore",
                "author": "Haruki Murakami",
                "genres": ["Magical Realism"],
                "ending_date": "2024-01-05"
            }
        ]
    }

    with patch("routes.statistics.get_readed_books_between_dates") as mock_service:
        mock_service.return_value = fake_response

        response = client.get(
            "/statistics/readed-books-specific-date?start_date=2024-01-01&end_date=2024-01-10"
        )

    assert response.status_code == 200
    data = response.get_json()
    assert data["results"][0]["book_title"] == "Kafka on the Shore"
