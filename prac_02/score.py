import random


def main():
    score = float(input("Enter score: "))
    determine_score_result(score)
    random_score = random.randint(0, 101)
    determine_score_result(random_score)


def determine_score_result(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif 50 < score < 90:
        print("Passable")
    elif score > 90:
        print("Excellent")
    else:
        print("Bad")


main()
