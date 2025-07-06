"""
Guitars program
"""
# My guitars!
# Name: Fender Stratocaster
# Year: 2014
# Cost: $765.4
# Fender Stratocaster (2014) : $765.40 added.
# Name:
# ... snip ...
# These are my guitars:
# Guitar 1:  Fender Stratocaster (2014), worth $    765.40
# Guitar 2:       Gibson L-5 CES (1922), worth $ 16,035.40 (vintage)
# Guitar 3:        Line 6 JTV-59 (2010), worth $  1,512.90

from prac_06.guitar import Guitar

def main():
    """Run and list guitars using Guitar class."""
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        try:
            name = input("Name: ")
        except NameError:
            print("Name must be a string.")

    year = input("Year: ")
    while year <= 0:
        try:
            year = int(input("Year: "))
        except ValueError:
            print("Year must be a number.")


main()