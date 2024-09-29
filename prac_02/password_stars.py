"""
get password
while password < 8
    get password
display '*' * length of password
"""
MINIMUM_LENGTH = 8

def main():
    password = input("Enter password: ")
    while len(password) < MINIMUM_LENGTH:
        password = input("Enter password: ")
    print('*' * len(password))


main()