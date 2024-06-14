import decimal
import requests


class LocationResolver:
    @staticmethod
    def resolve_address(address) -> tuple[decimal, decimal]:
        response = requests.get(
            'https://nominatim.openstreetmap.org/search',
            params={'q': address, 'format': 'json'},
            headers={'User-Agent': 'weatheralerter.kyleross.com'}
        )

        if response.status_code == 200:
            data = response.json()
            if data:
                latitude: decimal = data[0]['lat']
                longitude: decimal = data[0]['lon']
                return latitude, longitude
