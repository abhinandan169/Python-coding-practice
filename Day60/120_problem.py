# Create a class Book with a class variable total_books that tracks how many Book objects have been created. Each time a new Book is created, increase the count by 1.

class Book:
    total_books = 0

    def __init__(self):
        Book.total_books += 1

b1 = Book()
b2 = Book()
b3 = Book()
print(Book.total_books)        

