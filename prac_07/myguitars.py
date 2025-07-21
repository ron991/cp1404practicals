"""
CP1404 Practical 07 More Guitars!
Estimated time : 3 hours
Actual time :   hours
"""

import csv

from guitar import Guitar


def main():
    """Read file of guitars and store them in a list of guitar objects"""
    guitars = []
    with open('guitars.csv', 'r', newline='') as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            name = row[0]
            year = int(row[1])
            cost = float(row[2])

            guitars.append(Guitar(name, year, cost))
    guitars.sort()

    for guitar in guitars:
        print(guitar)


main()
