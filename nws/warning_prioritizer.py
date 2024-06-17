"""
This class is responsible for prioritizing the most immediate and severe weather alerts.
It uses the Severity and Urgency values from the Enums module to determine the priority of the alerts.
Alerts are sorted by severity first, then by urgency.

"""
from typing import Any

from nws_enums import Severity, Urgency
from weather_warning import WeatherWarning


def pick_most_important_warning(warnings: [WeatherWarning]) -> Any | None:
    """
    This function takes a list of WeatherWarning objects and returns the most important warning.
    The most important warning is determined by the severity and urgency of the warning.
    If two warnings have the same severity, the warning with the higher urgency is considered more important.
    If two warnings have the same severity and urgency, the first warning in the list is returned.

    :param warnings: A list of WeatherWarning objects
    :return: The most important WeatherWarning object
    """
    if not warnings:
        return None
    # Sort the warnings by severity and urgency
    warnings.sort(key=lambda w: (Severity[w.severity], Urgency[w.urgency]))

    # Return the last warning in the sorted list
    return warnings[-1]
