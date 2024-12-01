import random
from prac_09.car import Car


class UnreliableCar(Car):
    """An unreliable car that inherits from car."""

    def __init__(self, name, fuel, reliability):
        """Initialise variables."""
        super().__init__(name,fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if random generated number is less than reliability."""
        if random.randint(0,100) >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
