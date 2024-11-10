WELCOME_MESSAGE = "Welcome to Pythonic Project Management"
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
"""
LOAD_OPTION = 'L'
DISPLAY_OPTION = 'D'
FILTER_OPTION = 'F'
ADD_OPTION = 'A'
UPDATE_OPTION = 'U'
QUIT_OPTION = 'Q'


def main():
    print(WELCOME_MESSAGE)
    save_file()
    print(MENU)
    choice = input(">>> ")
    while choice != QUIT_OPTION:
        if choice == LOAD_OPTION:
            load_projects()
        elif choice == DISPLAY_OPTION:
            display_projects()
        elif choice == FILTER_OPTION:
            filter_projects()
        elif choice == ADD_OPTION:
            add_project()
        elif choice == UPDATE_OPTION:
            update_project()
        else:
            print("Invalid menu option, try again")
        print(MENU)
        choice = input(">>> ")


main()
