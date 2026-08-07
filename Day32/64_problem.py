# Create a class InsufficientBalanceError that inherits from Python's built-in Exception class. Create a BankAccount class with balance. In the withdraw(amount) method, if amount > balance, raise InsufficientBalanceError with a message like "Cannot withdraw {amount}, balance is only {balance}". Use a try-except block outside the class to test it (try withdrawing more than the balance and catch the error, printing the error message).


class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError(f"Can't withdraw {amount}, balance is only {self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}, remaining balance: {self.balance}") 


b = BankAccount(1000)

try:
    b.withdraw(5000)
except InsufficientBalanceError as e:
    print("Error:", e)               