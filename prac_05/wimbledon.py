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
    champion_wins, countries = process_data(data)
    display_champion_wins(champion_wins)


def read_data(filename):
    """read data from csv."""
    with open(filename, encoding="utf-8-sig") as infile:
        infile.readline()
        lines = [line.strip().split(',') for line in infile]
    return lines

def process_data(data):
    """process data from csv."""
    champion_wins = {}
    countries = set()
    for row in data:
        champion = row[2]
        country = row[1]
        countries.add(country)
        champion_wins[champion] = champion_wins.get(champion, 0) + 1
    return champion_wins,countries



main()



