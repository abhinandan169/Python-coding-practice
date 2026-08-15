# Create a Product class with attributes name and price. Create a list of 5 Product objects with different prices. Write a loop to find and print the name of the cheapest product (use comparison logic, no min()).

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

p1 = Product("Clothes", 1000)
p2 = Product("Footwear", 500)
p3 = Product("Watches", 2000)
p4 = Product("Sunglasses", 200)
p5 = Product("Mobiles", 18000)

products = [p1, p2, p3, p4, p5]

cheapest_product = products[0]

for product in products:
    if product.price < cheapest_product.price:
        cheapest_product = product


print(f"Cheapest Product: {cheapest_product.name}, Price: {cheapest_product.price}")        