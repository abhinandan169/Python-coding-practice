# Create a Vehicle class with attributes name, distance (in km), and fuel_used (in litres). Add a method mileage() that returns distance / fuel_used. Create 2 vehicle objects and print which one has better mileage.

class Vehicle:
    def __init__(self, name, distance, fuel_used):
        self.name = name
        self.distance = distance
        self.fuel_used = fuel_used

    def mileage(self):
        return self.distance / self.fuel_used

v1 = Vehicle("BMW M5", 50, 60)

v2 = Vehicle("Tata Sierra", 40, 30)


if v1.mileage() > v2.mileage():
    print(f"{v1.name} has better mileage: {v1.mileage()}")
else:
    print(f"{v2.name} has better mileage: {v2.mileage()}")    