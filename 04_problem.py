# Create a Rectangle class with a constructor that takes length and width. Add two methods — area() and perimeter() — that return the respective values.



class Rectangle:
        def __init__(self, length, width):
            self.length = length
            self.width = width

        def area(self):
            return  self.length * self.width

        def perimeter(self):
            return  2 * (self.length + self.width)
        
r = Rectangle(5 , 4)
print("Area", r.area())
print("Perimeter", r.perimeter())