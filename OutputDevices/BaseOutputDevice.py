from abc import ABC, abstractmethod


class BaseOutputDevice(ABC):
    @abstractmethod
    def output(self, output_string: str):
        pass
