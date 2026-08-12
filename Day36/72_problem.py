# Create an Item class with attributes name, price, and quantity. Add a method total_value() that returns price * quantity. Create 3 items and print the combined total value of all items (sum using a loop)

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

i1 = Item("Book", 150, 200)
i2 = Item("Pen", 30, 500)
i3 = Item("Pencil", 50, 150)

items = [i1, i2, i3]
total = 0

for item in items:
    total = total + item.total_value()

print(f"Total Values of all Items: {total}")        
