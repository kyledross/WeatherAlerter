import json
import os
from datetime import datetime, timedelta
from dateutil import parser
from dateutil.tz import tzutc


def current_time_utc() -> datetime:
    return datetime.now(tzutc())


def parse_time_to_utc(time_str: str) -> datetime:
    return parser.parse(time_str).astimezone(tzutc())


def is_throttled(same_code: str) -> bool:
    """
    Return True if the last processing time is less than a minute ago. Otherwise, return False.
    :return: True if throttled, False otherwise
    """
    # persist the last processing time in a file at ~/.kyledross/weather_alerter/persistent_data.json
    # the last time will be stored in a key-value pair called "last_processing_time"

    key_name = f"last_processing_time_{same_code}"
    user_home = os.path.expanduser("~")
    persistent_data_path = os.path.join(user_home, ".kyledross/weather_alerter")
    os.makedirs(persistent_data_path, exist_ok=True)
    persistent_data_pathname = os.path.join(persistent_data_path, "persistent_data.json")
    persistent_data = {}

    if os.path.exists(persistent_data_pathname):
        with open(persistent_data_pathname, "r") as file:
            persistent_data = json.load(file)

    current_time = current_time_utc()
    # default to current time plus 1 minute
    last_processing_time = current_time - timedelta(minutes=1)

    if key_name in persistent_data:
        last_processing_time = parse_time_to_utc(persistent_data[key_name])
    persistent_data[key_name] = current_time.isoformat()
    elapsed_time = current_time - last_processing_time
    if elapsed_time.total_seconds() < 60:
        return True
    else:
        with open(persistent_data_pathname, "w") as file:
            json.dump(persistent_data, file)
        return False
