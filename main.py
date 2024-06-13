# sudo apt-get install sense-hat
# sudo apt-get install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0
# pip install PyGObject



import importlib
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