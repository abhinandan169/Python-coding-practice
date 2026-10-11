# Create a class Account with attribute balance and a method show_balance() that prints the balance. Create a class SavingsAccount that inherits from Account, adds interest_rate, and overrides show_balance() to first call the parent's show_balance() using super(), then also print the interest rate.


class Account:
    def __init__(self, balance):
        self.balance = balance

    def show_balance(self):
        print("Balance:", self.balance)

class SavingsAccount(Account):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def show_balance(self):
        super().show_balance()
        print("Interest rate:", self.interest_rate)

s = SavingsAccount(10000, 4)
s.show_balance()