# Create a class Garage that stores a list of car names. Add methods add_car(name) to add a car, and remove_car(name) to remove a car from the list (if it exists).


class Garage:
    def __init__(self):
        self.cars = []

    def add_car(self, name):
        self.cars.append(name)

    def remove_car(self, name):
        if name in self.cars:
            self.cars.remove(name)


g = Garage()
g.add_car("Mercedes")
g.add_car("Range rover")
g.add_car("Defender")
g.add_car("BMW M5")
g.add_car("Mahindra Thar")
g.remove_car("Mercedes")
print(g.cars)               