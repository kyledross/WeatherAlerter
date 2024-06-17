from datetime import datetime


class WeatherWarning:
    def __init__(self, effective: datetime, expires: datetime, event: str, urgency: str, severity: str):
        self.__effective = effective
        self.__expires = expires
        self.__event = event
        self.__urgency = urgency
        self.__severity = severity

    @property
    def effective(self) -> datetime:
        return self.__effective

    @property
    def expires(self) -> datetime:
        return self.__expires

    @property
    def event(self) -> str:
        return self.__event

    @property
    def urgency(self) -> str:
        return self.__urgency

    @property
    def severity(self) -> str:
        return self.__severity
