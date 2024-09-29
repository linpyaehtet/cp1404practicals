"""
get password
while password < 8
    get password
display '*' * length of password
"""
MINIMUM_LENGTH = 8

def main():
    password = get_password()
    display_asterisks(password)


def display_asterisks(password):
    print('*' * len(password))


def get_password():
    password = input(f"Enter password ({MINIMUM_LENGTH} characters or more): ")
    while len(password) < MINIMUM_LENGTH:
        password = input(f"Enter password ({MINIMUM_LENGTH} characters or more): ")
    return password


main()