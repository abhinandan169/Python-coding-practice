# Create a Library class with an add_book(book_name) method that stores books in a list, and a show_books() method that prints all stored books.


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)  

    def show_books(self):
        print(self.books)

lib = Library()
lib.add_book("Rich DAD Poor DAD")
lib.add_book("Harry Potter")
lib.show_books()            