# Create an Engine class with attribute horsepower and a method start() that prints "Engine started with {horsepower} HP". Create a Car class that has an Engine object as an attribute (not inheritance — this is called "composition", i.e. Car "has-a" Engine). Add a method start_car() in Car that calls the engine's start() method. Create a Car object and call start_car().


class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine started with {self.horsepower} HP")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        self.engine.start()



e = Engine(150)
c = Car(e)
c.start_car()                