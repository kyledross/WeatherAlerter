import argparse

import utility
from nws.nws_data_fetcher import Fetcher
from nws.nws_location_resolver import LocationResolver
from nws.warning_prioritizer import pick_most_important_warning
from output_devices.device_factory import DeviceFactory


def get_warnings_using_coordinates(location_coordinates) -> []:
    fetcher = Fetcher()
    data = fetcher.get_json_from_nws_using_coordinates(location_coordinates[0], location_coordinates[1])
    return fetcher.get_warnings(data, utility.current_time_utc())


def get_warnings_using_same_code(same_code: str) -> []:
    zone_id = LocationResolver.resolve_same_code_to_zone_id(same_code)
    data = Fetcher.get_json_from_nws_using_zone_id(zone_id)
    return Fetcher.get_warnings(data, utility.current_time_utc())


def main() -> None:
    parser = argparse.ArgumentParser(description='Process location.')
    parser.add_argument('--same',
                        type=str,
                        required=True,
                        help='NWS SAME code to use, for example --same 012345')
    parser.add_argument('--output',
                        type=str,
                        default='cli',
                        choices=['cli', 'sensehat'],
                        help='Output method to use. If no output is specified, cli will be used. SenseHAT refers to '
                             'a Raspberry Pi with a Sense HAT device attached.')
    parser.add_argument('--persist-notification',
                        action='store_true',
                        help='Keep notification visible until it is no longer in effect. This behavior is dependent '
                             'on the chosen output type. For example, the cli output type does not persist any '
                             'notification, whereas the sensehat output type will display an exclamation point until '
                             'the program is run and there is no more alerts to display.')
    args = parser.parse_args()
    current_warnings = get_warnings_using_same_code(args.same)
    output_device = DeviceFactory.create_device(args.output)
    if current_warnings:
        most_important_warning = pick_most_important_warning(current_warnings)
        output_device.output(most_important_warning.event, args.persist_notification)
    else:
        # clear any previous notification
        output_device.clear_notification()


if __name__ == "__main__":
    main()
