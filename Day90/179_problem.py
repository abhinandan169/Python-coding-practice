# Create a class BankAccount with a class variable interest_rate = 4 and an instance variable balance. Add a method calculate_interest() that returns balance * interest_rate / 100. Create two accounts with different balances, print their interest, then change BankAccount.interest_rate to 5 and print the interest again.


class BankAccount:
    interest_rate = 4

    def __init__(self, balance):
        self.balance = balance

    def calculate_interest(self):
        return self.balance * BankAccount.interest_rate / 100

a1 = BankAccount(10000)
a2 = BankAccount(20000)

print(a1.calculate_interest())  
print(a2.calculate_interest())   

BankAccount.interest_rate = 5

print(a1.calculate_interest())   
print(a2.calculate_interest())   