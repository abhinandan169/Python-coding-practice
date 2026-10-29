# Create a class BankAccount with public owner and private __balance. Add deposit(amount) and get_balance(). Create SavingsAccount inheriting from it, with an extra rate attribute and a method add_interest() that adds interest to the balance using deposit().


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, rate):
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self):
        self.deposit(self.get_balance() * self.rate / 100)

s = SavingsAccount("Rahul", 10000, 5)
s.deposit(2000)
s.add_interest()
print(s.get_balance())