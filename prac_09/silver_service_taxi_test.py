from prac_09.silver_service_taxi import SilverServiceTaxi

fancy_taxi = SilverServiceTaxi("Hummer", 100, 2)
fancy_taxi.drive(18)
print(f"Fare: ${fancy_taxi.get_fare()}")
print(fancy_taxi)