# Create a Loan class with attributes principal, rate, and time. Add a method calculate_interest() that returns simple interest using the formula (principal × rate × time) / 100. Create 2 loan objects with different values and print their interest.


class Loan:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    def calculate_interest(self):
        return (self.principal * self.rate * self.time) / 100

l1 = Loan(10000, 5, 2)
print(f"Interest of Loan 1: {l1.calculate_interest()}")

l2 = Loan(50000, 8, 3)
print(f"Interest of Loan 2: {l2.calculate_interest()}")
