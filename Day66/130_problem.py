# Create a class BankAccount with a private attribute __balance. Use @property to create a balance getter that returns the balance, and use @balance.setter to allow setting the balance only if the new value is non-negative (otherwise print "Balance cannot be negative").

class BankAccount:
    def __init__(self):
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            print("Balance cannot be negative")

acc = BankAccount()
acc.balance = 1000
print(acc.balance)
acc.balance = -200  