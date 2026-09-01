# Create a class Temperature with attribute celsius. Add a method to_fahrenheit() that returns the temperature converted to Fahrenheit (formula: (celsius * 9/5) + 32).


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

t = Temperature(25)
print(t.to_fahrenheit())  