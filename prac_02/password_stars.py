"""
get password
while password < 8
    get password
display '*' * length of password
"""
password = input("Enter password: ")
while len(password) < 8:
    password = input("Enter password: ")
print('*' * len(password))