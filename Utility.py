from datetime import datetime
from dateutil import parser
from dateutil.tz import tzutc


def current_time_utc() -> datetime:
    return datetime.utcnow().astimezone(tzutc())


def parse_time_to_utc(time_str: str) -> datetime:
    return parser.parse(time_str).astimezone(tzutc())
