import importlib

from OutputDevices.BaseOutputDevice import BaseOutputDevice


class SenseHatDevice(BaseOutputDevice):
    _is_raspberry_pi = False

    try:
        sense_hat = importlib.import_module('sense_hat')
        _is_raspberry_pi = True
    except ModuleNotFoundError:
        sense_hat = importlib.import_module('sense_emu')

    sense = sense_hat.SenseHat()
    if _is_raspberry_pi:
        sense.set_rotation(180)
    sense.show_message("Hello World!")

    def output(self, output_string: str):
        pass
