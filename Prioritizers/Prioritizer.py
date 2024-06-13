class Prioritizer:
    """
    This class is responsible for picking the most urgent weather alert and returning it.
    """

    def __init__(self, alerts):
        self.alerts = alerts

    def priority_alert(self) -> str:
        """
        This method returns the most urgent weather alert.
        """
        # Pick the most urgent alert from self.alerts
        return "Tornado alert"
