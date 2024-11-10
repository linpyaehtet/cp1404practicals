from prac_07.guitar import Guitar

def main():
    guitars = read_file()
    display_guitars(guitars)

def read_file():
    guitars = []
    with open('guitars.csv', 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    return guitars


def display_guitars(guitars):
    guitars.sort()
    for guitar in guitars:
        print(guitar)


main()