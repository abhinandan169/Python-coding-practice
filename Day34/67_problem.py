# Create a Ticket class with attributes movie_name and price. Add a method apply_discount(percent) that reduces the price by that percentage (e.g., 10% discount on ₹200 → ₹180). Create an object and print the price before and after discount.

class Ticket:
    def __init__(self, movie_name, price):
        self.movie_name = movie_name
        self.price = price

    def apply_discount(self, percent):
        discount_amount = self.price * percent / 100
        self.price = self.price - discount_amount



t = Ticket("KGF", 280)
print("Before Discount:", t.price)

t.apply_discount(10)
print("After Discount:", t.price)