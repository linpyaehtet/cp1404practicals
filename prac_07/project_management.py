from prac_07.project import Project

WELCOME_MESSAGE = "Welcome to Pythonic Project Management"
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

PROJECT_COMPLETION_PERCENTAGE = 100
LOAD_OPTION = 'L'
SAVE_OPTION = 'S'
DISPLAY_OPTION = 'D'
FILTER_OPTION = 'F'
ADD_OPTION = 'A'
UPDATE_OPTION = 'U'
QUIT_OPTION = 'Q'

projects = []

def main():
    print(WELCOME_MESSAGE)
    load_projects()
    projects.sort()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != QUIT_OPTION:
        if choice == LOAD_OPTION:
            load_projects()
        elif choice == SAVE_OPTION:
            save_projects()
        elif choice == DISPLAY_OPTION:
            display_projects(projects)
        elif choice == FILTER_OPTION:
            filter_projects()
        elif choice == ADD_OPTION:
            add_project()
        elif choice == UPDATE_OPTION:
            update_project()
        else:
            print("Invalid menu option, try again")
        print(MENU)
        choice = input(">>> ").upper()


def display_projects(projects):
    incomplete_projects = []
    complete_projects = []
    for project in projects:
        if project.completion == PROJECT_COMPLETION_PERCENTAGE:
            complete_projects.append(project)
        else:
            incomplete_projects.append(project)
    print("Incomplete projects:")
    for incomplete_project in incomplete_projects:
        print(f"\t{incomplete_project}")
    print("Complete projects:")
    for complete_project in complete_projects:
        print(f"\t{complete_project}")

def load_projects():
    file_name = input("Enter the file name: ")
    with open (file_name, "r") as in_file:
        in_file.readline()
        lines = in_file.readlines()
        project_count = 0
        for line in lines:
            parts = line.strip().split('\t')
            projects.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))
            project_count += 1
    print(f"Loaded {project_count} projects from {file_name}")


main()
