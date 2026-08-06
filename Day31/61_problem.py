# Create a Point class with attributes x and y. Add a special method __add__(self, other) so that adding two Point objects with + returns a new Point with summed x and y. Also add __str__ to print it nicely as "(x, y)". Create 2 points and add them using +.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point (new_x, new_y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(3, 4)

p3 = p1 + p2

print(p3)