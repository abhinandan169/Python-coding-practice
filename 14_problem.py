# Create a Wallet class with a private attribute __amount. Add an add_money(amount) method and a spend_money(amount) method that checks if there are sufficient funds before spending.



class Wallet:
    def __init__(self, amount):
        self.__amount = amount

    def add_money(self, amount):
        self.__amount += amount
        print(f"{amount} added and New balance is {self.__amount}")


    def spend_money(self, amount):
        if amount > self.__amount:
            print("Insufficient funds")
        else:
            self.__amount -= amount
            print(f"{amount} spent. remaining balance is {self.__amount}")


w = Wallet(60000)
w.add_money(50000)
w.spend_money(70000)
w.spend_money(10000)
w.spend_money(35000)               
                    

   