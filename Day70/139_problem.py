# Create a class Order with attributes item and price. Create a class Cart that stores a list of Order objects. Add a method apply_discount(percent) that reduces the price of every order in the cart by that percent.


class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

class Cart:
    def __init__(self):
        self.orders = []

    def apply_discount(self, percent):
        for order in self.orders:
            discount_amount = order.price * percent / 100
            order.price = order.price - discount_amount

c = Cart()
c.orders.append(Order("Shoes", 1000))
c.orders.append(Order("Bag", 500))
c.apply_discount(10)

for order in c.orders:
    print(order.item, order.price)            