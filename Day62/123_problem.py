# Create a class Shape with a method draw() that prints "Drawing a shape". Create two classes Circle and Square that inherit from Shape, each overriding draw() to print "Drawing a circle" and "Drawing a square" respectively. Create a list containing one Circle object and one Square object, loop through it, and call draw() on each.


class Shape():
    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

shapes = [Circle(), Square()]

for shape in shapes:
    shape.draw()