"""
Email to name Dictionary
Estimate : 1 hour
Actual : 2 hours
"""


def main():
    """Create a dictionary of emails to names"""
    email_to_name = {}
    email = input("Enter your email address: ")
    while email != "":
        name = get_name_from_email(email)
        name_confirmation = input(f"Is your name {name}? (Y/N): ")
        if name_confirmation.upper() != "Y":
            name = input("Enter your name: ")
        email_to_name[email] = name
        email = input("Enter your email address: ")

    for email, name in email_to_name.items():
        print(f"{name}: {email}")
        for email in email_to_name.items():
            print(f"{name: {email[1]}}")


def get_name_from_email(email):
    """Get name from email"""
    prefix = email.split("@")[0]
    parts = prefix.split(".")
    name = ".".join(parts)
    return name

main()
