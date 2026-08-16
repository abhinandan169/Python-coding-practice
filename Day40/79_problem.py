# Create a Bill class with attributes food_amount and tax_percent. Add a method total_bill() that returns food_amount + (food_amount * tax_percent / 100). Create 2 bill objects with different values and print their totals.


class Bill:
    def __init__(self, food_amount, tax_percent):
        self.food_amount = food_amount
        self.tax_percent = tax_percent

    def total_bill(self):
        return self.food_amount + (self.food_amount * self.tax_percent / 100)


b1 = Bill(4000, 5)   
b2 = Bill(500, 18)

Bills = [b1, b2]
total = 0

for bill in Bills:
    print(f"Total Bill: {bill.total_bill()}") 