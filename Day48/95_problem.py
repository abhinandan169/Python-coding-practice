# Create a class Book with attributes title, author, and price. Add a method apply_discount(percent) that reduces the price by that percent and prints the new price.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def apply_discount(self, percent):
        discount_amount = self.price * percent / 100
        self.price = self.price - discount_amount
        print(self.price)

b1 = Book("Blind Love", "shri kant sharma", 500)
b1.apply_discount(10)