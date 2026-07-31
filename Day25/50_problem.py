# Create a Cart class with attribute items (an empty list). Add methods add_item(item) (adds item to list) and show_items() (prints all items). Create an object, add 3 items, then show them.


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        for item in self.items:
            print(item)


c = Cart()
c.add_item("Apple")
c.add_item("Milk")
c.add_item("Bread")
c.show_items()