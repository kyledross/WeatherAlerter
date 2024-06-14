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

location = LocationResolver.resolve_address("Callaway County, MO")
fetcher = Fetcher.Fetcher(location[0], location[1])
# data = fetcher.get_json_from_nws()
# Fetcher.save_json_to_file(data, './Tests/TestData/multiple_warning_response.json')
data = Fetcher.get_json_from_file('./Tests/TestData/multiple_warning_response.json')
warnings = Fetcher.get_warnings(data, Fetcher.Utility.parse_time_to_utc('2024-06-13T21:58:00-05:00'))
if warnings:
    print(pick_most_important_warning(warnings).event)

