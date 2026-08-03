# Create a parent class Vehicle with attributes brand and speed, and a method info() that prints "{brand} runs at {speed} km/h". Create a child class ElectricVehicle that inherits from Vehicle, adds an extra attribute battery_capacity, and overrides info() to also print "Battery: {battery_capacity} kWh" (call the parent's info() first using super(), then print the extra line).



class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def info(self):
        print(f"{self.brand} runs at {self.speed} km/h")

class ElectricVehicle(Vehicle):
    def __init__(self, brand, speed, battery_capacity):
        super().__init__(brand, speed)
        self.battery_capacity = battery_capacity

    def info(self):
        super().info()
        print(f"Battery: {self.battery_capacity} kWh")


ev = ElectricVehicle("Tesla", 200, 75)
ev.info()          
