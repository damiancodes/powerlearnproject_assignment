# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Defining a class
from rich.jupyter import display


class Car:
    color = "red"  # Attribute

    # Method
    def drive(self):
        print("The car is driving 🚗")

# Creating an object
my_car = Car()
print(my_car.color)
my_car.drive()


class Door:
    color = "red"

    def open(self):
        print("Open the door")

my_door = Door()
my_door.open()


class Blood:
    def __init__(self, color, type):
     self.color = color
     self.type = type

    def donate(self):
       print(f"We are doing a blood drive today {self.color} and {self.type}")

my_blood = Blood("red", "0+")
my_blood.donate()
# another_blood = Blood(color= "dark red, type = A")
# another_blood.donate()


class oil:
    def __init__(self, color, price, quality):
        self.color = color
        self.price = price
        self.quality = quality

    def product(self):
        print(f"The product of oil in japan {self.color} is {self.price} {self.quality}")

my_oil = oil("red", "300ksh", quality="high")
my_oil.product()



class smartphone:
    def __init__(self, color, price, quality):
        self.color = color
        self.price = price
        self.quality = quality

    def Oppo(self):
        print(f"The product of smartphone {self.color} is {self.price} {self.quality}")

my_smartphone = smartphone("red", "300ksh", quality="high")
my_smartphone.Oppo()


# Parent class
class Smartphones:
    def __init__(self, color, price, quality, brand):
        self.color = color
        self.price = price
        self.quality = quality
        self.brand = brand

    # Getter methods
    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def get_quality(self):
        return self.quality

    def get_brand(self):
        return self.brand

    # Display method
    def display(self):
        print(f"{self.brand} smartphone - Color: {self.color}, Price: {self.price}, Quality: {self.quality}")


# Child class inheriting from Smartphones
class Oppo(Smartphones):
    def __init__(self, color, price, quality, battery_life):
        super().__init__(color, price, quality, "Oppo")
        self.battery_life = battery_life  # New attribute specific to Oppo

    # Overriding display method
    def display(self):
        print(f"Oppo Smartphone - Color: {self.color}, Price: {self.price}, Quality: {self.quality}, Battery Life: {self.battery_life} hours")










