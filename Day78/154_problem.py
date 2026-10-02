# Create a class Product with attributes name and price. Add a __str__ method that returns "<name>: ₹<price>". Create a list of 3 products and print each one using a loop.


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ₹{self.price}"


p1 = Product("Nescafe", 130)
p2 = Product("TATA Premium Tea", 150)
p3 = Product("Good Day Biscuits", 40)


product = [p1, p2, p3]

for p in product:
    print(p)