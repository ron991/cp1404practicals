"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
# A value error will occur when the input is not a valid integer for either the numerator or denominator.
2. When will a ZeroDivisionError occur?
#Will happen when the denominator is zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes by adding a loop to ask for a non-zero denominator before the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")