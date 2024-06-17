# implement base class for CLI devices
from OutputDevices.BaseOutputDevice import BaseOutputDevice


class CLIDevice(BaseOutputDevice):
    def output(self, output_string: str):
        print(output_string)