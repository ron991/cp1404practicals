"""
Test the unreliable car.
"""


from prac_09.unreliable_car import UnreliableCar

def main():
    """Test the unreliable car."""

    bad_car = UnreliableCar("Needs work", 100, 30)

    for i in range(1,10):
        print(f"Test drive {i}km: ")
        print(f"{bad_car:12} drove {bad_car.drive(i):2}km")

    print(bad_car)


main()