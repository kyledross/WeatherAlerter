# sudo apt-get install sense-hat
# sudo apt-get install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0
# pip install PyGObject

#


# https://alerts.weather.gov/search

import argparse
from LocationResolver import LocationResolver
from OutputDevices import DeviceFactory
from Prioritizer import pick_most_important_warning
import Fetcher


def get_warnings_using_coordinates(location_coordinates) -> []:
    fetcher = Fetcher.Fetcher()
    data = fetcher.get_json_from_nws_using_coordinates(location_coordinates[0], location_coordinates[1])
    return Fetcher.get_warnings(data, Fetcher.Utility.current_time_utc())


def get_warnings_using_same_code(same_code: str) -> []:
    zone_id = LocationResolver.resolve_same_code_to_zone_id(same_code)
    fetcher = Fetcher.Fetcher()
    data = fetcher.get_json_from_nws_using_zone_id(zone_id)
    return Fetcher.get_warnings(data, Fetcher.Utility.current_time_utc())


def main() -> None:
    parser = argparse.ArgumentParser(description='Process location.')
    parser.add_argument('--same', type=str, required=True, help='NWS SAME code to use')
    parser.add_argument('--output', type=str, default='cli', choices=['cli', 'sensehat'], help='Output method to use')
    args = parser.parse_args()
    current_warnings = get_warnings_using_same_code(args.same)
    output_device = DeviceFactory.DeviceFactory.create_device(args.output)
    if current_warnings:
        most_important_warning = pick_most_important_warning(current_warnings)
        output_device.output(most_important_warning.event)


if __name__ == "__main__":
    main()
