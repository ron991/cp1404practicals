"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if 0 < score > 100:
    print("Invalid score")
elif score < 50:
    print("Bad")
elif 50 <= score <= 90:
    print("Passable")
else:
    print("Excellent")
