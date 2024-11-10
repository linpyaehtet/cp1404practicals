class Project:
    def __init__(self, name="", date="", priority=0, cost_estimate=0, completion=0):
        self.name = name
        self.date = date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def __str__(self):
        return f"{self.name}, start: {self.date}, priority: {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion}%"

    def __lt__(self, other):
        return self.priority < other.priority