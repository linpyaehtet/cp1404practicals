from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
MENU = "q)uit, c)hoose taxi, d)rive"
QUIT_OPTION = 'Q'
CHOOSE_OPTION = 'C'
DRIVE_OPTION = 'D'


def main():
    current_taxi = None
    bill_to_date = 0
    print("Let's drive!")
    print(MENU)
    user_choice = input(">>> ").upper()
    while user_choice != QUIT_OPTION:
        if user_choice == CHOOSE_OPTION:
            print("Taxis available")
            display_taxis()
            chosen_taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[chosen_taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif user_choice == DRIVE_OPTION:
            if current_taxi:
                drive_taxi(current_taxi)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                bill_to_date += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        user_choice = input(">>> ").upper()
    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis()


def drive_taxi(current_taxi):
    current_taxi.start_fare()
    distance = float(input("Drive how far? "))
    current_taxi.drive(distance)


def display_taxis():
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()


