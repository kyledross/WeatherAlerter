from output_devices.cli_device import CLIDevice
from output_devices.sense_hat_device import SenseHatDevice


class DeviceFactory:
    @staticmethod
    def create_device(device_type: str):
        if device_type == 'cli':
            return CLIDevice()
        elif device_type == 'sensehat':
            return SenseHatDevice()
        else:
            raise ValueError(f"Unknown device type: {device_type}")
