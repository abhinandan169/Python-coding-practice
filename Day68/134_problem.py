# Create a class Vehicle with method start() printing "Vehicle started". Create Car inheriting from Vehicle with method drive() printing "Car driving". Create SportsCar inheriting from Car with method turbo() printing "Turbo boost". Create a SportsCar object and call all three methods.


class Vehicle:
    def start(self):
        print("Vehicle Started")

class Car(Vehicle):
    def drive(self):
        print("Car driving")

class SportsCar(Car):
    def turbo(self):
        print("Turbo boost")

s = SportsCar()
s.start()
s.drive()
s.turbo()                        