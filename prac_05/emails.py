"""
Emails
Estimated time to complete: 2 hours
Actual time to complete:
"""

def main():
    """Create dictionary of emails to names"""
    email_to_name = {}
    email = input("Enter email: ")
    while email != "":
        name_part = email.split("@")[0]
        name_parts = name_part.replace('.', ' ').split()
        name = " ".join(name_parts).title()

        confirmation = input(f"Is your name {name}? (Y/n) ").lower()
        if confirmation not in ("", "y"):
            email = input("Enter email: ")

        email_to_name[email] = name
        email = input("Enter email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()


