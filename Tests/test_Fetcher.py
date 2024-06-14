import unittest
from datetime import datetime, timezone

import Prioritizer
from Fetcher import Fetcher, get_warnings, get_json_from_file
from WeatherWarning import WeatherWarning


class TestFetcher(unittest.TestCase):

    def setUp(self) -> None:
        self.fetcher = Fetcher(0, 0)

    def test_get_warning(self) -> None:
        current_time: datetime = datetime(2024, 6, 13, 20, 30, tzinfo=timezone.utc)
        data = get_json_from_file('./TestData/single_warning_response.json')
        self.assertIsInstance(data, dict)
        result = get_warnings(data, current_time)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], WeatherWarning)
        self.assertEqual(result[0].effective, datetime(2024, 6, 13, 20, 20, tzinfo=timezone.utc))
        self.assertEqual(result[0].expires, datetime(2024, 6, 13, 21, 0, tzinfo=timezone.utc))
        self.assertEqual(result[0].event, 'Severe Thunderstorm Warning')
        self.assertEqual(result[0].urgency, 'Immediate')

    def test_get_expired_warning(self) -> None:
        current_time: datetime = datetime(2024, 6, 13, 22, 00, tzinfo=timezone.utc)
        data = get_json_from_file('TestData/single_warning_response.json')
        self.assertIsInstance(data, dict)
        result = get_warnings(data, current_time)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_prioritizer_with_multiple_warnings(self) -> None:
        current_time: datetime = datetime(2024, 6, 14, 2, 58, tzinfo=timezone.utc)
        data = get_json_from_file('./TestData/multiple_warning_response.json')
        self.assertIsInstance(data, dict)
        result = get_warnings(data, current_time)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)

        most_urgent = Prioritizer.pick_most_important_warning(result)
        self.assertIsInstance(most_urgent, WeatherWarning)

        self.assertEqual(most_urgent.effective, datetime(2024, 6, 14, 2, 57, tzinfo=timezone.utc))
        self.assertEqual(most_urgent.expires, datetime(2024, 6, 14, 3, 15, tzinfo=timezone.utc))
        self.assertEqual(most_urgent.event, 'Tornado Warning')
        self.assertEqual(most_urgent.urgency, 'Immediate')
        self.assertEqual(most_urgent.severity, 'Extreme')
