## This is my activity 2 
# Its about Polymorphism Challenge
# Different classes define the same action move() differently.

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying through the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water ⛵")

# Demonstrate polymorphism
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        v.move()  # each call invokes the class-specific move()
