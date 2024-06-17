from abc import ABC, abstractmethod


class BaseOutputDevice(ABC):
    @abstractmethod
    def output(self, output_string: str, persist_notification: bool) -> None:
        """
        Will output the given string to the device.
        :param persist_notification: True if the notification should be persistent, False otherwise.
        :param output_string: The string to output
        :return: None
        """
        pass

    def clear_notification(self) -> None:
        """
        Will clear any persistent notification on the device, if the device supports it.
        :return: None
        """
        pass
