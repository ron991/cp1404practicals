"""
Test the unreliable car.
"""


from prac_09.unreliable_car import UnreliableCar

def main():
    """Test the unreliable car."""

    bad_car = UnreliableCar("Bomb", 100, 10)
    average_car = UnreliableCar("toyota", 100, 90)


    for i in range(1,11):
        print(f"Test drive {i}km: ")
        print(f"{average_car.name:12} drove {average_car.drive(i):2}km")
        print(f"{bad_car.name:12} drove {bad_car.drive(i):2}km")


    print(bad_car)
    print(average_car)


main()