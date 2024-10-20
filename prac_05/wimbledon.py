def main():
    filename = 'wimbledon.csv'
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = [line.strip() for line in in_file.readlines()]


main()