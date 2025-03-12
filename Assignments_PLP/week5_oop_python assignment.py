# Parent class
class Smartphone:
    def __init__(self, brand, color, price, quality):
        self.brand = brand
        self.color = color
        self.__price = price
        self.quality = quality  

    # Getter for price (Encapsulation)
    def get_price(self):
        return self.__price

    # Setter for price (Encapsulation)
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price cannot be negative!")

    # Method to display smartphone details
    def display_details(self):
        print(f"{self.brand} smartphone - Color: {self.color}, Price: {self.__price}, Quality: {self.quality}")


# Child class inheriting from Smartphone
class Oppo(Smartphone):
    def __init__(self, color, price, quality, battery_life):
        super().__init__("Oppo", color, price, quality)
        self.battery_life = battery_life  # Additional attribute for Oppo phones

    # Overriding the method to include battery life
    def display_details(self):
        print(f"Oppo Smartphone - Color: {self.color}, Price: {self.get_price()}, Quality: {self.quality}, Battery Life: {self.battery_life} hours")


# Creating instances
my_smartphone = Oppo("Red", 30000, "High", 24)
my_smartphone.display_details()

# Updating price using encapsulation
my_smartphone.set_price(35000)
my_smartphone.display_details()
