# Create a Book class with attributes title and __is_borrowed (private, boolean, default False). Add methods borrow_book() that sets it to True (and prints "Book borrowed" — or "Already borrowed" if it's already True), and return_book() that sets it back to False (and prints "Book returned").


class Book:
    def __init__(self, title):
        self.title = title
        self.__is_borrowed = False

    def borrow_book(self):
        if self.__is_borrowed == True:
            print("Already Borrowed")
        else:
            self.__is_borrowed = True
            print("Book Borrowed")    

    def return_book(self):
        self.__is_borrowed = False
        print("Book returned")

b = Book("Harry potter")
b.borrow_book()
b.return_book()
b.borrow_book()