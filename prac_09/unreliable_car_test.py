from prac_09.unreliable_car import UnreliableCar

# Unreliable car test
unreliable_car = UnreliableCar("Prius 1", 100, 10)
reliable_car = UnreliableCar("Prius 2", 100, 90)

for i in range(3):
    print(f"{unreliable_car.name} drove {unreliable_car.drive(30)}km")
    print(f"{reliable_car.name} drive {reliable_car.drive(30)}km")
    print()