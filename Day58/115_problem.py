# Create a class Wallet with attribute balance (starting at 0). Add methods deposit(amount) and withdraw(amount). If withdrawal amount is more than balance, print "Insufficient balance" instead of allowing it.


class Wallet:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit: {amount} and balance is: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdraw: {amount} and remainning: {self.balance}")

w = Wallet()
w.deposit(150000)
w.deposit(5000)
w.withdraw(15000)