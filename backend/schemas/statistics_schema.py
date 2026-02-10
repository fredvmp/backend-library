from datetime import datetime, date
from utils.errors import ValidationError


def parse_date_range(args):
    start_date_str = args.get("start_date")
    end_date_str = args.get("end_date")

    if not start_date_str:
        raise ValidationError("start_date is required (yyyy-mm-dd)")

    start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()

    if end_date_str:
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
    else:
        end_date = date.today()

    return start_date, end_date
