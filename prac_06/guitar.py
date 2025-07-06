"""
Guitar class for guitar test and guitars program
"""

CURRENT_YEAR = 2025
VINTAGE_AGE = 50


class Guitar:
    """Guitar class for guitar information."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Represent a string Guitar instance."""
        return f"{self.name} {self.year} : ${self.cost}"

    def get_age(self):
        """Get the age of the Guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE
