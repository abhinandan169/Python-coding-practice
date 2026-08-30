# Create a class Inventory that stores items as a dictionary (item name → quantity). Add a method add_item(name, qty) that adds a new item or increases quantity if it already exists.


class Inventory:
    def __init__(self):
       self.items = {}

    def add_item(self, name, qty):
        if name in self.items:
            self.items[name] = self.items[name] + qty
        else:
            self.items[name] = qty

inv = Inventory()
inv.add_item("Shoes", 10)
inv.add_item("Shoes", 5)
inv.add_item("Bag", 3)
print(inv.items)           