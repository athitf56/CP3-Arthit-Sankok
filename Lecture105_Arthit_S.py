class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Car(Vehicle):
    pass;

class PickUp(Vehicle):
    pass;

class Van(Vehicle):
    pass;

class EstateCar(Vehicle):
    pass;

car1 = Car()
car1.turnOnAirConditioner()
print("Car")

PickUp1 = PickUp()
PickUp1.turnOnAirConditioner()
print("PickUp")

Van1 = Van()
Van1.turnOnAirConditioner()
print("Van")

EstateCar1 = EstateCar()
EstateCar1.turnOnAirConditioner()
print("EstateCar")