# Create a Product class with attributes name and price. Add a special method __str__(self) that returns a formatted string like "Product: {name}, Price: ₹{price}". Create 2 objects and simply print() them directly (not calling any method — just print(obj)).


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name}, price: {self.price}"


p1 = Product("Ghee", 1400)
print(p1)

p2 = Product("Wheat", 40)
print(p2)