# Create a BankAccount class with attribute balance (starting at 0). Add two methods: deposit(amount) which adds money to balance, and withdraw(amount) which subtracts money (but should not allow balance to go negative — print "Insufficient funds" if it would). Test it with a few deposits and withdrawals.


class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} and Balance: {self.balance} ")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdraw {amount} and remaining balance is {self.balance}")


b = BankAccount()
b.deposit(80000)
b.withdraw(500)
b.withdraw(1000)
b.deposit(2000)