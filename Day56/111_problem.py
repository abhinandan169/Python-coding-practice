# Create a class Rectangle with attributes length and width. Add a method is_square() that returns True if the rectangle is actually a square (length equals width), otherwise False.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def is_square(self):
        if self.length == self.width:
            return True
        else:
            return False

r1 = Rectangle(5, 5)
print(r1.is_square())

r2 = Rectangle(5, 8)
print(r2.is_square())

