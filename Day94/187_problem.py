# Create a class ATM with a private attribute __pin and a private method __verify(pin) that returns True if the pin matches. Add a public method withdraw(pin, amount) that prints "Withdrawn <amount>" if the pin is correct, otherwise "Wrong PIN".


class ATM:
    def __init__(self, pin):
        self.__pin = pin

    def __verify(self, pin):
        return self.__pin == pin

    def withdraw(self, pin, amount):
        if self.__verify(pin):
            print(f"Withdrawn {amount}")
        else:
            print("Wrong PIN")

atm = ATM(1234)
atm.withdraw(1234, 500)
atm.withdraw(1111, 500)