import decimal
import json
from datetime import datetime

import requests

import Utility
from WeatherWarning import WeatherWarning


def get_warnings(data: dict, current_time: datetime) -> [WeatherWarning]:
    # Create a list to store the warnings
    warnings = []

    # Iterate over the features in the data
    for feature in data['features']:
        # Check if the status is 'Actual' and the severity is 'Severe'
        if feature['properties']['status'] == 'Actual' and feature['properties']['category'] == 'Met':
            effective_time = Utility.parse_time_to_utc(feature['properties']['effective'])
            expires_time = Utility.parse_time_to_utc(feature['properties']['expires'])
            if effective_time <= current_time < expires_time:
                event = feature['properties']['event']
                urgency = feature['properties']['urgency']
                severity = feature['properties']['severity']
                warnings.append(WeatherWarning(effective_time, expires_time, event, urgency, severity))

    return warnings


def get_json_from_file(pathname: str) -> dict:
    with open(pathname) as f:
        data = json.load(f)
    return data


def save_json_to_file(data: dict, pathname: str) -> None:
    with open(pathname, 'w') as f:
        json.dump(data, f)


class Fetcher:

    def get_json_from_nws_using_coordinates(self, latitude: decimal, longitude: decimal) -> dict:
        # Construct the URL for the latitude and longitude
        url = f"https://api.weather.gov/alerts/active?point={latitude},{longitude}"
        # Send a GET request to the URL
        response = requests.get(url, headers={'User-Agent': 'weatheralerter.kyleross.com'})
        # Parse the response content as JSON
        return response.json()

    def get_json_from_nws_using_zone_id(self, zone_id: str) -> dict:
        # Construct the URL for the latitude and longitude
        url = f"https://api.weather.gov/alerts/active/zone/{zone_id}"
        # Send a GET request to the URL
        response = requests.get(url, headers={'User-Agent': 'weatheralerter.kyleross.com'})
        # Parse the response content as JSON
        return response.json()
