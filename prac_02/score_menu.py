"""
display menu
get choice
while choice != <quit option>
    if choice == <first option>
        <do first task>
    else if choice == <second option>
        <do second task>
    ...
    else if choice == <n-th option>
        <do n-th task>
    else
        display invalid input error message
    display menu
    get choice
<do final thing, if needed>
"""

MENU = """  
(G) - Get a valid score (must be 0 - 100 inclusive)
(P) - Print result
(S) - Show stars
(Q) - Quit
"""


def main():
    score = 0
    while score == 0:
        score = int(input("Enter a valid score (must be 0 - 100 inclusive): "))
        while score < 0 or score > 100:
            print("Invalid entry , try again!")
            score = int(input("Enter a valid score (must be 0 - 100 inclusive"))
        menu_choice = main_menu()
        while menu_choice != "Q":

            if menu_choice == "G":
                print_result(score)
                main_menu()
            elif menu_choice == "P":
                print_result(score)
                main_menu()
            elif menu_choice == "S":
                show_stars(score)
                main_menu()
            elif menu_choice == "Q":
                print("Farewell")
            else:
                print("Invalid choice")

            print()


def print_result(score):
    result = get_result(score)
    print("Result:", result)


def show_stars(score):
    print("*" * score)


def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif 50 < score < 90:
        return "Passable"
    elif score > 90:
        return "Excellent"
    else:
        return "Bad"


def main_menu():
    menu_choice = input("(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit\nChoose an option: ").upper()
    return menu_choice

main()
