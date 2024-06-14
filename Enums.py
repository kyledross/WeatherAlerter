from enum import IntEnum


class Urgency(IntEnum):
    Past = 0
    Future = 1
    Expected = 2
    Immediate = 3


class Severity(IntEnum):
    Unknown = 0
    Minor = 1
    Moderate = 2
    Severe = 3
    Extreme = 4
