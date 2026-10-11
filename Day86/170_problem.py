# Create a class Vehicle with attributes brand and year. Create a class Bike that inherits from Vehicle and adds an attribute cc. Use super().__init__() in Bike. Add a method show() in Bike that prints brand, year, and cc.


class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

class Bike(Vehicle):
    def __init__(self, brand, year, cc):
        super().__init__(brand, year)
        self.cc = cc

    def show(self):
        print(self.brand, self.year, self.cc)

b = Bike("Royal Enfield", 2023, 350)
b.show()   