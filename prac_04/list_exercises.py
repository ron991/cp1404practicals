# Write a program that prompts the user for 5 numbers and then stores each of these in a list called numbers.
# The program should then output information about these numbers, as in the output below.
# You can use the functions min, max, sum and len, and you can use the append method to add a number to a list.

#
# Number: 5
# Number: 20
# Number: 1
# Number: 2
# Number: 3
# The first   number is 5
# Thelastnumber is 3
# Thesmallestnumber is 1
# Thelargestnumber is 20
# The average of the numbers is 6.2


numbers = []
for i in range(5):
    number = int(input("Enter the number: "))
    numbers.append(number)


print(f"The first number is: {numbers[0]}")
print(f"The last number is: {numbers[-1]}")
print(f"The largest number is: {max(numbers)}")
print(f"The average sum of numbers: {sum(numbers)}")
print(f"The average sum of numbers: {sum(numbers)/len(numbers)}")