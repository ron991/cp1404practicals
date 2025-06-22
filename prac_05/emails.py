"""
Emails
Estimated time to complete: 2 hours
Actual time to complete: 1 hour
"""

def main():
    """Create dictionary of emails to names"""
    email_to_name = {}
    email = input("Enter email: ")
    while email != "":
        name = extract_name_from_email(email)

        confirmation = input(f"Is your name {name}? (Y/n) ").lower()
        if confirmation not in ("", "y"):
           name = input("Name: ")

        email_to_name[email] = name
        email = input("Enter email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    name_part = email.split("@")[0]
    name_parts = name_part.replace('.', ' ').split()
    name = " ".join(name_parts).title()
    return name


main()


