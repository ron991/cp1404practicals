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
    display_results(champion_wins, countries)



def read_data(filename):
    """read data from a csv file and return list (excluding header)."""
    with open(filename,"r", encoding="utf-8-sig") as infile:
        infile.readline()
        lines = [line.strip().split(',') for line in infile]
    return lines

def process_data(data):
    """process data from csv into win counts and country list."""
    champion_wins = {}
    countries = set()
    for row in data:
        champion = row[2]
        country = row[1]
        countries.add(country)
        champion_wins[champion] = champion_wins.get(champion, 0) + 1
    return champion_wins,countries

def display_results(champion_wins, countries):
    """display champion win results with countries."""
    print("Wimbledon Champions:")
    for name, count in champion_wins.items():
        print(f"{name}: {count}")
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))


main()



