# Using the Circle and Square classes from Q57, create a list containing one Circle object and one Square object. Loop through the list and call area() on each — notice how the same method name gives different results depending on the object type (this is called polymorphism).


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


cr = Circle(4)
sq = Square(5)

shapes = [cr, sq]

for shape in shapes:
    print(shape.area())