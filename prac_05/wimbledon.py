FILENAME = 'wimbledon.csv'
CHAMPION_INDEX = 2
CHAMPION_COUNTRY_INDEX = 1

champion_to_count = {}
countries = set()

def main():
    """Read csv file and print the results of winners and their countries"""
    entries = load_data()
    process_entries(entries)


def load_data():
    """Load data into a list of lists"""
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        entries = [line.strip().split(",") for line in in_file.readlines()]
    return entries


def process_entries(entries):
    """Assign keys and values to the dictionary and countries to the set"""
    for entry in entries:
        countries.add(entry[CHAMPION_COUNTRY_INDEX])
        champion = entry[CHAMPION_INDEX]
        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1


main()