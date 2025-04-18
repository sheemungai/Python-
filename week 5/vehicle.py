class Vehicle:
    def move(self):
        print("The car is moving")

class Plane:
    def move(self):
        print("The plain is flying")

class Ship:
    def move (self):
        print("The ship is sailing")

for transport in (Vehicle(), Plane(), Ship()):
    transport.move()
    