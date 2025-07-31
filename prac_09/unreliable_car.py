"""
Unreliable Car Class.
"""
from prac_06.car import Car
from random import randint

class UnreliableCar(Car):
    """The unreliable car class."""

    def __init__(self, name, fuel, reliability):
        """Initialization of the car class."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car according to the distance based on the reliability."""
        random_number = randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven