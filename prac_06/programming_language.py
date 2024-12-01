"""
CP1404/CP5632 Practical - programming_language
Estimated time = 5 mins
Actual time taken = 5 mins
"""
class ProgrammingLanguage:
    def __init__(self, language="", typing="", reflection=False, year=0):
        """Initialize variables"""
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return the string representation of the Programming language"""
        return f"{self.language}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Return a boolean based on whether the type is dynamic"""
        return self.typing == "Dynamic"