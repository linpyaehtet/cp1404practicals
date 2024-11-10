# import csv
from prac_07.guitar import Guitar

def main():
    guitars = read_file()


def read_file():
    guitars = []
    with open('guitars.csv', 'r') as in_file:
        # reader = csv.reader(in_file)  # use default dialect, Excel
        for line in in_file:
            parts = line.strip().split(',')
            guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    return guitars


read_file()