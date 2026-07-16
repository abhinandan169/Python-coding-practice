# Create a Vehicle class with a private attribute __speed. Add a method accelerate(amount) that increases the speed, but should not allow speed to exceed 120 (print "Max speed limit reached" if it does).



class Vehicle:
    def __init__(self):
        self.__speed = 0

    def accelerate(self, amount):
        if self.__speed + amount > 120:
            print("Max limit reached")
        else:
            self.__speed += amount
            print(f"Speed is now {self.__speed}")


v = Vehicle()
v.accelerate(70)
v.accelerate(100)
v.accelerate(85)
v.accelerate(60)           






          