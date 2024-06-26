# pip install PyGObject
# If using Sense HAT: pip install sense-hat
# If using Sense HAT Emulator: pip install sense-emu

import importlib

from output_devices.base_output_device import BaseOutputDevice


class SenseHatDevice(BaseOutputDevice):

    def output(self, output_string: str, persist_notification: bool) -> None:
        """
        Will output the given string to the SenseHat or SenseEmu device.
        :param output_string: The string to output
        :param persist_notification: Will display a persistent ! notification if True
        :return:
        """
        is_raspberry_pi, sense = self.get_sense_hat()

        if is_raspberry_pi:
            sense.set_rotation(180)
        sense.show_message(output_string, text_colour=[255, 0, 0], scroll_speed=0.08)
        if persist_notification:
            self.set_notification()

    @staticmethod
    def get_sense_hat() -> (bool, object):
        is_raspberry_pi = False
        try:
            sense = importlib.import_module('sense_hat')
            is_raspberry_pi = True
        except ModuleNotFoundError:
            sense = importlib.import_module('sense_emu')
        return is_raspberry_pi, sense.SenseHat()

    def set_notification(self) -> None:
        """
        Will set a persistent ! notification on the SenseHat or SenseEmu device.
        :return: None
        """
        is_raspberry_pi, sense = self.get_sense_hat()

        if is_raspberry_pi:
            sense.set_rotation(180)
        sense.show_letter("!", text_colour=[255, 0, 0])

    def clear_notification(self) -> None:
        """
        Will clear any persistent notification on the SenseHat or SenseEmu device.
        :return: None
        """

        is_raspberry_pi, sense_hat = self.get_sense_hat()

        sense = sense_hat.SenseHat()
        if is_raspberry_pi:
            sense.set_rotation(180)
        sense.clear()
