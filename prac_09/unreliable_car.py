"""
Unreliable Car Class.
"""
from prac_06.car import Car

class UnreliableCar:
    """The unreliable car class."""

    def __init__(self, name, fuel, reliability):
        """Initialization of the car class."""
        super().__init__(name, fuel)
        self.reliability = reliability
