# Create a Product class with attributes name and price. Create a list of 5 Product objects. First calculate the average price of all products, then loop again to count and print how many products have price above the average.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

p1 = Product("TATA 1mg", 200)
p2 = Product("Perfume", 1500)
p3 = Product("Whey protein", 3500)
p4 = Product("Amul Butter", 199)
p5 = Product("Shampoo", 85)

products = [p1, p2, p3, p4, p5]
total = 0

for product in products:
    total = total + product.price

average = total / len(products)

print("The total average is:", average)

count = 0

for product in products:
    if product.price > average:
        count += 1

print("Product above average:", count)        