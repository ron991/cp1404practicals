"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    """Get a numeric score and display its result"""
    score = float(input("Enter score: "))
    print(determine_result(score))


def determine_result(score):
    """Determine the result of a given score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
