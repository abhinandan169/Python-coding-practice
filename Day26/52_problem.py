# Create a Book class with attributes title and is_available (default True). Create a Library class with attribute books (empty list). Add methods add_book(book) (adds a Book object to list), and borrow_book(title) (finds the book by title, if is_available is True, set it to False and print "Borrowed {title}", else print "{title} is not available").


class Book:
    def __init__(self, title):
        self.title = title
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_available:
                    book.is_available = False
                    print(f"Borrowed {title}")
                else:
                    print(f"{title} is not available")


b1 = Book("The Flamingo")
b2 = Book("The Harry Potter")

l = Library()
l.add_book(b1)
l.add_book(b2)

l.borrow_book("The Flamingo")
l.borrow_book("The Harry Potter")

l.borrow_book("The Flamingo")



