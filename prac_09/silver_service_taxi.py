from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Create class for Silver Service Taxi"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialize variables for Silver Service Taxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of the Silver Service Taxi"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip"""
        return self.flagfall + super().get_fare()