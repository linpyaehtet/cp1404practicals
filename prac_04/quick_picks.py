import random

RANDOM_NUMBER_AMOUNT = 6
MINIMUM = 1
MAXIMUM = 45

number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    random_numbers = []
    for j in range(RANDOM_NUMBER_AMOUNT):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in random_numbers:
            number = random.randint(MINIMUM, MAXIMUM)
        random_numbers.append(number)
    random_numbers.sort()
    print(" ".join(f"{number:2}" for number in random_numbers))
