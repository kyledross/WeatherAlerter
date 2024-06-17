# implement base class for CLI devices
from OutputDevices.BaseOutputDevice import BaseOutputDevice


class CLIDevice(BaseOutputDevice):
    def output(self, output_string: str, persist_notification: bool) -> None:
        """
        Will output the given string to the device.
        :param output_string: The string to output
        :param persist_notification: Not supported on CLI devices
        :return:
        """

        print(output_string)