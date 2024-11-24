from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

current_taxi = None
taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

print("Let's drive!")
print("q)uit, c)hooose taxi, d)rive")
user_choice = input(">>> ")
