# Create a class Circle with attribute radius. Add a method area() that returns the area of the circle (formula: 3.14 * radius * radius), and a method perimeter() that returns the perimeter (formula: 2 * 3.14 * radius).


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

c1 = Circle(5)
print(c1.area())

c2 = Circle(5)
print(c2.perimeter())