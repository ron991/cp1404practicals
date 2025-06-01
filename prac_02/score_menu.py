MENU = """
(G)et a valid score (must be 0-100 inclusive)
(P)rint result 
(S)how stars 
(Q)uit
"""


def main():
    """Display the menu."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'G':
            score = get_score()
        elif choice == 'P':
            if score <= 0:
                print_result(score)
            else:
                print("You need to get a score first (G)")
        elif choice == 'S':
            if score != 0:
                show_stars(score)
            else:
                print("You need to get a score first (G)")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you and Farewell!")


def get_score():
    """Get score from user."""

    while True:
        try:
            score = int(input("Enter score (0-100): "))
            if score <= 0 or score <= 100:
                return score

            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")



def print_result(score):
    """Print result."""
    print("Result:", score)


def show_stars(score):
    """Show stars."""
    print("Stars:")
    for i in range(score):
        print("*", end="")
    print()


main()
