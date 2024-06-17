import decimal
import json
import os
import csv

import requests


class LocationResolver:
    @staticmethod
    def resolve_address(location) -> tuple[decimal, decimal]:

        response = requests.get(
            'https://nominatim.openstreetmap.org/search',
            params={'q': location, 'format': 'json'},
            headers={'User-Agent': 'weatheralerter.kyleross.com'}
        )

        if response.status_code == 200:
            data = response.json()
            if data:
                latitude: decimal = data[0]['lat']
                longitude: decimal = data[0]['lon']
                return latitude, longitude
            else:
                raise ValueError(f'Location "{location}" not found.')
        else:
            raise ValueError(f'Failed to resolve location "{location}".')

    @staticmethod
    def resolve_address_with_cache(location) -> tuple[decimal, decimal]:
        if not location or location == '':
            raise ValueError('Location is required.  Ex: --location "New York, NY"')

        dir_path = os.path.expanduser('~/.WeatherAlerter')
        pathname = os.path.join(dir_path, 'location_cache.json')
        data = {}

        if os.path.exists(pathname):
            with open(pathname, 'r') as f:
                data = json.load(f)

        if location in data:
            return data[location]['latitude'], data[location]['longitude']

        latitude, longitude = LocationResolver.resolve_address(location)

        data[location] = {
            'latitude': latitude,
            'longitude': longitude
        }

        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        with open(pathname, 'w') as f:
            json.dump(data, f, indent=4)

        return latitude, longitude

    @staticmethod
    def resolve_same_code_to_zone_id(same_code: str) -> str:
        if same_code.startswith('0'):
            same_code = same_code[1:]
        path_to_data = "./data/bp05mr24.dbx.txt"
        with open(path_to_data, 'r') as f:
            reader = csv.reader(f, delimiter='|')
            for row in reader:
                if row[6] == same_code:
                    return f"{row[0]}Z{row[1]}"
