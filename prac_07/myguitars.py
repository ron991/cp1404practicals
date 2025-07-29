"""
CP1404 Practical 07 More Guitars!
Estimated time : 3 hours
Actual time :   hours
"""

import csv

from guitar import Guitar


def main():
    """Read file of guitars and store them in a list of guitar objects"""
    print("My guitars.")
    guitars = []
    with open('guitars.csv', 'r', newline='') as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            name = row[0]
            year = int(row[1])
            cost = float(row[2])

            guitars.append(Guitar(name, year, cost))
    guitars.sort()

    add_guitar(guitars)

    for guitar in guitars:
        print(guitar)

def add_guitar(guitar):
    """Add a guitar to the list of guitars"""
    print("Add new guitar: ")
    while True:
        name = input("Name: ")
        if name == "":
            return

        is_valid_input = False
        while not is_valid_input:
            try:
                year = int(input("Year: "))
                cost = float(input("Cost: "))
                is_valid_input = True
            except ValueError:
                print("Invalid input. Please enter a valid year and cost. ")

        new_guitar = (Guitar(name, year, cost))
        guitar.append(new_guitar)
        print(f"{name} ({year}) : ${cost:.2f} added.\n")


main()
