# Create a parent class Shape with a method area() that just prints "Area not defined" (a generic placeholder). Create two child classes Circle (with attribute radius) and Square (with attribute side), each overriding area() to return the correct area (π×r² for circle — use 3.14; side×side for square). Create one object of each and print their areas.



class Shape:
    def area(self):
        print("Area not defined")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


cr = Circle(2)
sq = Square(4)

print(cr.area())
print(sq.area())

         