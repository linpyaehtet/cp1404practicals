email_to_name = {}

email = input("Email: ")
while email != "":
    name = email.split("@")[0]
    email_to_name[email] = name
    email = input("Email: ")
