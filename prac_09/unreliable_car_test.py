from prac_09.unreliable_car import UnreliableCar

# Unreliable car test
unreliable_car = UnreliableCar("Prius 1", 100, 10)
unreliable_car.drive(30)
print(unreliable_car)

#Reliable car test
reliable_car = UnreliableCar("Prius 2", 100, 90)
reliable_car.drive(30)
print(reliable_car)