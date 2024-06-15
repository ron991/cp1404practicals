numbers = []
for i in range(5):
    number = int(input("Enter a number: "))
    numbers.append(number)

print(f"The first number is {numbers[0]}")
print(f"The second number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
get_username = input("Enter a username: ")
while get_username not in usernames:
    print("Invalid username!")
    get_username = input("Enter a username: ")
    if get_username in usernames:
        print("Access granted!")
    else:
        print("Access denied!")
