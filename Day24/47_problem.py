# Create a Rectangle class with attributes length and width. Add two methods: area() (returns length × width) and perimeter() (returns 2 × (length + width)). Create an object and print both.



class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width 

    def area(self):  
        return self.length * self.width 

    def perimeter(self):
        return 2 * (self.length + self.width)


r = Rectangle(4, 5)
print(r.area())
print(r.perimeter())