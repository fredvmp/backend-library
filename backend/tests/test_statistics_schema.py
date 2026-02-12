from schemas.statistics_schema import parse_date_range
from datetime import date
import pytest
from utils.errors import ValidationError


# Test 1: correcto
def test_parse_date_range_valid(): 
    args = {
        "start_date": "2024-01-01",
        "end_date": "2024-01-10"
    }

    start, end = parse_date_range(args)

    assert start.isoformat() == "2024-01-01"
    assert end.isoformat() == "2024-01-10"


# Test 2: sin end_date
def test_parse_date_range_without_end_date():
    args = {"start_date": "2024-01-01"}

    start, end = parse_date_range(args)

    assert start.isoformat() == "2024-01-01"
    assert isinstance(end, date)


# test 3: sin start_date (error)
def test_parse_date_range_missing_start_date():
    args = {}

    with pytest.raises(ValidationError):
        parse_date_range(args)


# Test 4: mal formato (error)
def test_parse_date_range_invalid_format():
    args = {"start_date": "01-01-2024"}

    with pytest.raises(ValueError):
        parse_date_range(args)
