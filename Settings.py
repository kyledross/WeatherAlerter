import json
import os


class Settings:
    def __init__(self, county, state):
        self.county = county
        self.state = state

    def to_dict(self):
        return {
            'county': self.county,
            'state': self.state
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['county'], data['state'])

    def save(self):
        path = os.path.expanduser('~/.weatherwarn/settings.json')
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            json.dump(self.to_dict(), f, indent=4)

    @classmethod
    def load(cls):
        path = os.path.expanduser('~/.weatherwarn/settings.json')
        with open(path, 'r') as f:
            data = json.load(f)
        return cls.from_dict(data)
