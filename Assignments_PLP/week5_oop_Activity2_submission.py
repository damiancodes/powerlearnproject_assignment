
class Vehicle:
    def move(self):
        pass


# Child classes with different move() behaviors

class Car(Vehicle):
    def move(self):
        print(" Driving on the road!")

class Plane(Vehicle):
    def move(self):
        print(" Flying in the sky!")

class Boat(Vehicle):
    def move(self):
        print(" Sailing on the water!")

class Train(Vehicle):
    def move(self):
        print(" Running on the tracks!")


# Using Polymorphism
vehicles = [Car(), Plane(), Boat(), Train()]

for v in vehicles:
    v.move()  # Each object calls its own move() method
