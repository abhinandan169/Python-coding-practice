# Temperature class banao jisme private __celsius ho. to_fahrenheit() method banao jo convert karke Fahrenheit return kare (formula: F = (C * 9/5) + 32), aur get_celsius() method banao jo celsius value return kare.


# (C * 9/5) + 32)

class Temperature:
    def __init__(self, celsius):
        self.__celsius =  celsius

    def to_fahrenheit(self):
        return (self.__celsius * 9/5) + 32

    def get_celsius(self):
        return self.__celsius


t = Temperature(45)
print("Fahrenheit:", t.to_fahrenheit())
print("Celsius:", t.get_celsius())      