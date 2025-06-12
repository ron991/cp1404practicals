# Write a program that asks the user how many "quick picks" they wish to generate. The program then generates that many lines of output. Each line consists of 6 random numbers between 1 and 45.
# These values should be stored as CONSTANTS.
#
# Each line (quick pick) should not contain any repeated number.
# Each line of numbers should be displayed in sorted (ascending) order.
# Study the formatting below so that numbers align neatly.
# Note
#
# Python's random module has a sample() function, which returns a selection from a list.
# This is a nice way to solve this problem... but it's too easy :)
# Do not use it for this program.
#
# Your code should produce output that matches this sample output (except the numbers are random):
#
# How many quick picks? 5
#  1 12 14 15 30 36
#  2  5  8 33 38 41
#  2 12 19 22 29 43
# 13 21 28 29 42 43
#  3  4 10 11 32 44


import random

MINIMUM = 1
MAXIMUM = 45
NUMBERS_PER_LINE = 6


def main():
    number_of_quick_picks = int(input("How many quick picks would you like? "))
    while number_of_quick_picks < 0:
        print("Please enter a positive integer.")
        number_of_quick_picks = input("How many quick picks would you like?")

    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        # print(" ".join(map(str, quick_pick)))
        # Had to refer to solution ; Difficult
        print(" ".join(f"{number}" for number in quick_pick))

main()
