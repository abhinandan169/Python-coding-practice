# Using the same Book class, create a list of 3 books and print the whole list in one print() call (not with a loop). Notice how each book shows up inside the list.


class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __repr__(self):
        return f"Book({self.title}, {self.price})"

books = [
    Book("Python Basics", 450),
    Book("Java Basics", 500),
    Book("C++ Basics", 400),
]

print(books)