# Create a Car class with attributes brand and __mileage (private, in km). Add a method drive(km) that increases the mileage, and a method get_mileage() that returns the current mileage. Also add a __str__ method that prints "Car: [brand], Mileage: [mileage] km".



class Car:
    def __init__(self, brand):
        self.brand = brand
        self.__mileage = 0

    def drive(self, km):
        self.__mileage += km

    def get_mileage(self):
        return self.__mileage

    def __str__(self):
        return f"Car: {self.brand}, Mileage: {self.__mileage} km"



car = Car("Mercedes Benz")
car.drive(90)
car.drive(65)
print(car.get_mileage())
print(car)