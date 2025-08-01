"""
Silver Service Taxi class
"""

from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A silver service taxi class from taxi"""
    flagfall = 4.50


    def __init__(self, name, fuel, fanciness):
        """Initialize the Silver Service taxi class"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of the taxi"""
        return f"{self.name}, fuel = {self.fuel}, odo={self._odometer}, {self.current_fare_distance} km on current fare, ${self.price_per_km:.2f}/km plus flagfall of {self.flagfall:.2f}"

    def get_fare(self):
        """Calculate the fare"""
        return self.flagfall + super().get_fare()

