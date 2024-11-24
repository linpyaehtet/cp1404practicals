from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

current_taxi = None
taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
MENU = "q)uit, c)hooose taxi, d)rive"
QUIT_OPTION = 'Q'
CHOOSE_OPTION = 'C'
DRIVE_OPTION = 'D'
bill_to_date = 0

print("Let's drive!")
print(MENU)
user_choice = input(">>> ").upper()
while user_choice != QUIT_OPTION:
    if user_choice == CHOOSE_OPTION:
        print("Taxis available")
        for i,taxi in enumerate(taxis):
            print(f"{i} - {taxi}")
        chosen_taxi_choice = int(input("Choose taxi: "))
        try:
            current_taxi = taxis[chosen_taxi_choice]
        except IndexError:
            print("Invalid taxi choice")
        print(f"Bill to date: ${bill_to_date:.2f}")
    elif user_choice == DRIVE_OPTION:
        distance = int(input("Drive how far? "))
        trip_cost = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
        bill_to_date += trip_cost
    else:
        print("Invalid option")
    print(MENU)
    user_choice = input(">>> ").upper()


