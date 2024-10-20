FILENAME = 'wimbledon.csv'
CHAMPION_INDEX = 2
CHAMPION_COUNTRY_INDEX = 1

champion_to_count = {}
countries = set()

def main():
    """Read csv file and print the results of winners and their countries"""
    entries = load_data()
    print(entries)


def load_data():
    """Load data into a list of lists"""
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        entries = [line.strip().split(",") for line in in_file.readlines()]
    return entries


main()