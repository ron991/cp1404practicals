MINIMUM_LENGTH = 4

def main():
    """Get and print password"""
    password = get_password(MINIMUM_LENGTH)
    print_stars(password)


def get_password(minimum_length):
    """Get password that meets minimum length requirement."""
    password = input(f"Enter a password of at least {minimum_length} characters: ")
    while len(password) < minimum_length:
        print("Password must be at least ", minimum_length)
    return password

def print_stars(sequence):
    """Print sequence of stars."""
    print('*' * len(sequence))


main()