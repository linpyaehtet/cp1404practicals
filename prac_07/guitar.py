"""
CP1404/CP5632 Practical - guitar
"""
CURRENT_YEAR = 2022
VINTAGE_AGE_THRESHOLD = 50
class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialize variables"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return the string representation of the guitar"""
        return f"{self.name} ({self.year}) : {self.cost}"

    def get_age(self):
        """Get the age of a guitar by subtracting from the current year"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage or not based on age"""
        return self.get_age() >= VINTAGE_AGE_THRESHOLD