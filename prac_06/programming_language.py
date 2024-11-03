class ProgrammingLanguage:
    def __init__(self, language="", typing="", reflection=False, year=0):
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"