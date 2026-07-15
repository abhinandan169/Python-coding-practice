# Create a Shape parent class with a describe() method. Create Square and Circle child classes that override describe() to print their own message (demonstrating Polymorphism).


class Shape:
    def describe(self):
        print("This is a Shape")

class Square(Shape):
    def describe(self):
        print("This is a square")


class Circle(Shape):
    def describe(self):
        print("This is a Circle")        


sh = Shape()
sh.describe()

sq = Square()
sq.describe()

cr = Circle()
cr.describe()