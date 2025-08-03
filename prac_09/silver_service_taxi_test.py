"""
Silver service taxi tests.
"""
from prac_09 import taxi
from  prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Test drive the silver service taxi."""

    taxi = SilverServiceTaxi('Hummer', 200, 4)
    taxi.drive(100)
    print(taxi)

    test_fare()


def test_fare():
    """Test if the fare is correct."""
    taxi = SilverServiceTaxi('Fancy Taxi', 200, 2)
    taxi.start_fare()
    taxi.drive(18)
    fare = taxi.get_fare()
    expected_fare = 48.78

    print(f"Calculated fare: ${fare:.2f}")
    assert abs(fare - expected_fare) < 0.01, f"Expected fare to be ${expected_fare:.2f}, but got ${fare:.2f}"
    print("Test finished.")


main()