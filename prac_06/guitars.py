"""
Guitars program
"""

from prac_06.guitar import Guitar


def main():
    """Run and list guitars using Guitar class."""
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        valid_year = False
        while not valid_year:
            try:
                year = int(input("Year: "))
                if year > 0:
                    valid_year = True
                else:
                    print("Year must be > 0")
            except ValueError:
                print("Invalid input.")
        valid_cost = False
        while not valid_cost:
            try:
                cost = float(input("Cost: "))
                if cost > 0:
                    valid_cost = True
                else:
                    print("Cost must be > 0")
            except ValueError:
                print("Cost must be a number.")

        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)

        print(f"{guitar_to_add}, added.")
        name = input("Name: ").strip()

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print("These are my guitars: ")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""

            if guitar.is_vintage():
                vintage_string = "vintage" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")
    else:
        print("No guitars.")


main()
