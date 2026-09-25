# Create an abstract class Payment with an abstract method pay(amount). Create two classes CreditCard and UPI that inherit from Payment, each implementing pay(amount) to print a different message (e.g., "Paid <amount> via Credit Card").


from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} via Credit Card")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} via UPI") 

c = CreditCard()
c.pay(5000)

u = UPI()
u.pay(2000)