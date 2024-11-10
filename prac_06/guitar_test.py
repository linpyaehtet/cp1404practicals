"""
CP1404/CP5632 Practical - guitar_test.
Estimated time = 5 mins
Actual time taken = 15 mins
"""
from prac_06.guitar import Guitar
first_guitar = Guitar("Gibson L-5 CES", 1922)
second_guitar = Guitar("Another Guitar", 2013)
print(f"{first_guitar.name} get_age() - Expected 100. Got {second_guitar.get_age()}")
print(f"{second_guitar.name} get_age() - Expected 9. Got {second_guitar.get_age()}")
print(f"{first_guitar.name} is_vintage() - Expected True. Got {second_guitar.is_vintage()}")
print(f"{second_guitar.name} is_vintage() - Expected False. Got {second_guitar.is_vintage()}")
