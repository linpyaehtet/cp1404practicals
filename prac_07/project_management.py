"""
Estimated time : 1 hour
Actual time taken : 3 hours
"""
from prac_07.project import Project
import datetime

WELCOME_MESSAGE = "Welcome to Pythonic Project Management"
GOODBYE_MESSAGE = "Thank you for using custom-built project management software."
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

LOAD_OPTION = 'L'
SAVE_OPTION = 'S'
DISPLAY_OPTION = 'D'
FILTER_OPTION = 'F'
ADD_OPTION = 'A'
UPDATE_OPTION = 'U'
QUIT_OPTION = 'Q'
SAVE_FILE_CHOICE = 'Y'

projects = []

def main():
    print(WELCOME_MESSAGE)
    load_projects()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != QUIT_OPTION:
        if choice == LOAD_OPTION:
            load_projects()
        elif choice == SAVE_OPTION:
            save_projects()
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
        choice = input(">>> ").upper()
    user_save_choice = input("Would you like to save to projects.txt?(y/n) ").upper()
    if user_save_choice == SAVE_FILE_CHOICE:
        save_projects()
    print(GOODBYE_MESSAGE)


def save_projects():
    file_name = input("File name to save projects: ")
    with open (file_name, "w") as out_file:
        out_file.write(f"Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage")
        for project in projects:
            out_file.writelines(f"{project.name}\t{project.date}\t{project.priority}\t{project.cost_estimate}\t{project.completion}\n")
    print(f"Projects saved to {file_name}.")


def filter_projects():
    filter_date_string = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(filter_date_string, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.date >= filter_date]
    filtered_projects.sort(key=lambda project: project.date)
    for project in filtered_projects:
        print(project)


def add_project():
    print("Let's add a new project")
    name = input("Name: ")
    start_date_string = input("Start date (dd/mm/yy): ")
    start_date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    project = Project(name, start_date, priority, cost_estimate, completion)
    projects.append(project)


def update_project():
    count = 0
    for project in projects:
        print(f"{count} {project}")
        count += 1
    project_choice = int(input("Project choice: "))
    print(projects[project_choice])
    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")
    projects[project_choice].completion = int(new_percentage)
    if new_priority != "":
        projects[project_choice].priority = int(new_priority)


def display_projects():
    incomplete_projects = []
    complete_projects = []
    for project in projects:
        if project.is_completed():
            complete_projects.append(project)
        else:
            incomplete_projects.append(project)
    print("Incomplete projects:")
    incomplete_projects.sort()
    for incomplete_project in incomplete_projects:
        print(f"\t{incomplete_project}")
    print("Complete projects:")
    complete_projects.sort()
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
            date = datetime.datetime.strptime(parts[1], '%d/%m/%Y').date()
            projects.append(Project(parts[0], date, int(parts[2]), float(parts[3]), int(parts[4])))
            project_count += 1
    print(f"Loaded {project_count} projects from {file_name}")


main()
