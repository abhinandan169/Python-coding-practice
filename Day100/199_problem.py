# Create an abstract class Shape with an abstract method area(). Create Circle (radius, formula 3.14 * r * r) and Rectangle (length, width). Put one of each in a list and print the area of every shape using a loop.


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(shape.area())