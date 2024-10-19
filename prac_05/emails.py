email_to_name = {}

def main():
    email = input("Enter your email: ")
    while email != "":
        name = extract_name_from_email(email)
        response = input(f"Is your name {name.title()}? (Y/n) ").upper()
        if response != "Y" and response != "":
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Enter your email: ")
    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    full_name = email.split('@')[0]
    name_parts = full_name.split('.')
    return " ".join(name_parts).title()


main()