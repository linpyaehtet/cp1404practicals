FILENAME = 'wimbledon.csv'
CHAMPION_INDEX = 2
CHAMPION_COUNTRY_INDEX = 1

def main():
    champion_to_count = {}
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        entries = [line.strip().split(",") for line in in_file.readlines()]
    print(entries)

    for entry in entries:
        champion = entry[CHAMPION_INDEX]
        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1
    print("Wimbledon Champions:")
    for champion, count in champion_to_count.items():
        print(f"{champion} {count}")


main()