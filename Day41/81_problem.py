# Create a Book class with attributes title and days_late. Add a method calculate_fine() that returns days_late * 2 (₹2 fine per day late). If days_late is 0 or less, fine should be 0. Create a list of 3 books and print each one's fine.

class Book:
    def __init__(self, title, days_late):
        self.title = title
        self.days_late = days_late

    def calculate_fine(self):
        if self.days_late <= 0:
            return 0
        else:
            return self.days_late * 2


b1 = Book("Harry Potter", 299)
b2 = Book("Python Basics", 0)
b3 = Book("DSA Guide", 499)

books = [b1, b2, b3]

for book in books:
    print(f"{book.title}: Fine = ₹{book.calculate_fine()}")
        