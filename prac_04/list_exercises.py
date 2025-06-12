

# Basic List Operations
numbers = []
for i in range(5):
    number = int(input("Enter the number: "))
    numbers.append(number)

print(f"The first number is: {numbers[0]}")
print(f"The last number is: {numbers[-1]}")
print(f"The smallest number is: {min(numbers)}")
print(f"The largest number is: {max(numbers)}")
print(f"The average sum of numbers: {sum(numbers)}")

# Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Enter the username: ")
if username in usernames:
    print(f"Access granted: {username}.")
else:
    print(f"Access denied: {username}.")

