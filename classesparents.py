#parent
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print(f"VROOM")

#childe
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("kaboom")

class Plane(Vehicle):
    def move(self):
        print("whoosh")

car = Car("Toyota", "ferrari")
boat = Boat("Yamaha", "speedboat")
plane = Plane("Boeing", "747")

for x in (car, boat, plane):
    print(x.brand)
    print(x.model)
    x.move()