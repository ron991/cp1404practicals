"""
Wimbledon
Estimated time to complete: 2 hours
Actual time to complete:
"""
import csv

FILENAME = "wimbledon.csv"


def main():
    """Read data and print details of wimbledon champions and what countries have won."""
    data = read_data(FILENAME)

def read_data(filename):
    """read data from csv."""
    with open(filename, encoding="utf-8-sig") as infile:
        infile.readline()
        #test
        print(infile.readline())

main()



