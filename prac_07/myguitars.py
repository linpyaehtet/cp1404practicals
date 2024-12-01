from prac_07.guitar import Guitar
FILE_NAME = "guitars.csv"

def main():
    guitars = read_file()
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        print(f"{name} ({year}) : ${cost:.2f} added.")
        guitars.append(Guitar(name, year, cost))
        print()
        name = input("Name: ")
    display_guitars(guitars)
    save_file(guitars)


def read_file():
    guitars = []
    with open(FILE_NAME, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    return guitars


def display_guitars(guitars):
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def save_file(guitars):
    with open(FILE_NAME, 'w') as out_file:
        for guitar in guitars:
            line = f"{guitar.name},{guitar.year},{guitar.cost}\n"
            out_file.write(line)


main()