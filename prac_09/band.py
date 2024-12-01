class Band:
    """Band class"""
    def __init__(self, name=""):
        """Construct a band with a name and a list of musicians"""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to the Band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing all musicians in the band playing their instruments."""
        return "\n".join(musician.play() for musician in self.musicians)

