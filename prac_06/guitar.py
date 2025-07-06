"""
Guitar class for guitar test and guitars program
"""


class Guitar:
    """Guitar class for guitar information."""


    def __init__(self, name ="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Represent a string Guitar instance."""
        return f"{self.name} {self.year} : ${self.cost}"

    def get_age(self):
        """Get the age of the Guitar."""
        return

    def is_vintage(self):
