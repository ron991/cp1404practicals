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
        name_parts = email.split("@")[0]
        name_parts = name_part.replace('.', ' ').split()
        name = " ".join(name_parts).title()


