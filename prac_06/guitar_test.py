"""
Guitar tests from guitar.py
"""

from prac_06.guitar import Guitar, CURRENT_YEAR

#
# name = "Gibson L-5 CES"
# year = 1922
# cost = 16035.40
# print(f"My guitar: {name}, first made in {year}")

CURRENT_YEAR = 2025


def run_tests():
    """Test for guitar class."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name,year,cost)

    print(f"{guitar.name} get_age() - Expected {100}. Got {guitar.get_age()}")




if __name__ == "__main__":
    run_tests()