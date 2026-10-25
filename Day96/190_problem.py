# Create a class Book with attributes title and price. Add a __repr__ method that returns "Book(<title>, <price>)". Create an object and print it.


class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __repr__(self):
        return f"Book({self.title}, {self.price})"

b = Book("Python Basics", 450)
print(b)