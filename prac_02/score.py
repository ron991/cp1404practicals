"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    determine_result(score)

    random_score = random.randint(1, 100)
    print(f"Random score:  {random_score}")
    determine_result(random_score)


def determine_result(score):
    if 0 < score > 100:
        print("Invalid score")
    elif score < 50:
        print("Bad")

    elif 50 <= score <= 90:
        print("Passable")
    else:
        print("Excellent")


main()
