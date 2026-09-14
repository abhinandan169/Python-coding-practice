# Create a class Library that stores a dictionary of book names and their available copies. Add a method borrow_book(name) that decreases the copies by 1 if available, otherwise prints "Not available".



class Library:
    def __init__(self):
        self.books = {"Python": 3, "Java": 0, "C++": 2}

    def borrow_book(self, name):
        if self.books[name] > 0:
            self.books[name] = self.books[name] - 1
        else:
            print("Not available")

lib = Library()
lib.borrow_book("Python")
print(lib.books)
lib.borrow_book("Java")            