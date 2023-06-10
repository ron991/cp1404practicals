def main():
    password = get_password()
    while len(password) < 5 or len(password) > 20:
        print("password not long enough")
    else:
        print("*" * len(password))


def get_password():
    password = input("Enter password : ")
    return password


main()
