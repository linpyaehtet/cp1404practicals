"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
HELLO_OPTION = "H"
GOODBYE_OPTION = "G"
QUIT_OPTION = "Q"
MENU = "(H)ello \n(G)oodbye \n(Q)uit"

name = input("Enter name: ")
print(MENU)
choice = input(">>> ").upper()
while choice != QUIT_OPTION:
    if choice == HELLO_OPTION:
        print(f"Hello {name}")
    elif choice == GOODBYE_OPTION:
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished.")