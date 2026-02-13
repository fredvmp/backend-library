from datetime import date
from services.statistics_service import get_readed_books_between_dates
from unittest.mock import patch


def test_get_readed_books_between_dates():
    start = date(2024, 1, 1)
    end = date(2024, 1, 10)

    fake_rows = [
        (1, "Kafka on the Shore", "Haruki Murakami", ["Magical Realism"], date(2024, 1, 5)),
        (2, "1984", "George Orwell", ["fiction"], date(2024, 1, 7)),
    ]

    # Mock de la función de DB
    with patch("services.statistics_service.fetch_readed_books_in_specific_date") as mock_fetch:
        mock_fetch.return_value = fake_rows
        result = get_readed_books_between_dates(start, end)

    assert result["start_date"] == "2024-01-01"
    assert result["end_date"] == "2024-01-10"
    assert len(result["results"]) == 2
    assert result["results"][0]["book_title"] == "Kafka on the Shore"


