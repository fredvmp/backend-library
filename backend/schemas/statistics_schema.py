from datetime import datetime, date


def parse_date_range(args):
    start_date_str = args.get("start_date")
    end_date_str = args.get("end_date")

    if not start_date_str:
        raise ValueError("start_date is required (yyyy-mm-dd)")

    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
        end_date = (
            datetime.strptime(end_date_str, "%Y-%m-%d").date()
            if end_date_str
            else date.today()
        )
    except ValueError:
        raise ValueError("Invalid date format. Use yyyy-mm-dd")

    return start_date, end_date
