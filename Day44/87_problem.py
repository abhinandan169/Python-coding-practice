# Create a Coupon class with attributes code and discount_percent. Add a method apply(amount) that returns the final amount after applying the discount (amount - (amount * discount_percent / 100)). Create 2 coupons and test them on different amounts.


class Coupon:
    def __init__(self, code, discount_percent):
        self.code = code
        self.discount_percent = discount_percent

    def apply(self, amount):
        self.amount = amount
        return self.amount - (self.amount * self.discount_percent / 100)

c1 = Coupon(4567, 10)
print(c1.apply(1000))

c2 = Coupon(8732, 7)
print(c2.apply(2000))
