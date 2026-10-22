# Create a class CoffeeMachine with private methods __boil_water() and __add_coffee(), each printing a step. Add a public method make_coffee() that calls both and then prints "Coffee ready". Call only make_coffee() on an object.


class CoffeeMachine:
    def __boil_water(self):
        print("Boiling water")

    def __add_coffee(self):
        print("Adding coffee")

    def make_coffee(self):
        self.__boil_water()
        self.__add_coffee()
        print("Coffee ready")

cm = CoffeeMachine()
cm.make_coffee()