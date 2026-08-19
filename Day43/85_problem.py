# Create an ElectricityBill class with attributes units_consumed. Add a method calculate_bill() that charges ₹5 per unit if units ≤ 100, else ₹8 per unit for all units (simple flat rate, not slab-based). Create a list of 3 bills with different units and print each one's total.

class ElectricityBill:
    def __init__(self, units_consumed):
        self.units_consumed = units_consumed

    def calculate_bill(self):
        if self.units_consumed <= 100:
            return self.units_consumed * 5
        else:
            return self.units_consumed * 8

b1 = ElectricityBill(85)               
b2 = ElectricityBill(160)               
b3 = ElectricityBill(100)

bills = [b1, b2, b3]

for bill in bills:
    print(f"Units: {bill.units_consumed}, Total Bills: {bill.calculate_bill()}")