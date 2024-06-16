# sudo apt-get install sense-hat
# sudo apt-get install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0
# pip install PyGObject

#
# _is_raspberry_pi = False
#
# try:
#     sense_hat = importlib.import_module('sense_hat')
#     _is_raspberry_pi = True
# except ModuleNotFoundError:
#     sense_hat = importlib.import_module('sense_emu')
#
# sense = sense_hat.SenseHat()
# if _is_raspberry_pi:
#     sense.set_rotation(180)
# sense.show_message("Hello World!")

# https://alerts.weather.gov/search


import Fetcher
from LocationResolver import LocationResolver
from Prioritizer import pick_most_important_warning

location = "Brooks, GA"


def get_warnings() -> []:
    location_coordinates = LocationResolver.resolve_address_with_cache(location)
    fetcher = Fetcher.Fetcher(location_coordinates[0], location_coordinates[1])
    data = fetcher.get_json_from_nws()
    return Fetcher.get_warnings(data, Fetcher.Utility.current_time_utc())


current_warnings = get_warnings()
if current_warnings:
    print(pick_most_important_warning(current_warnings).event)
