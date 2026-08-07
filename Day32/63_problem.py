# Create a Temperature class with attribute celsius. Add a property method fahrenheit (using @property) that calculates and returns celsius * 9/5 + 32 — so it can be accessed like an attribute (t.fahrenheit), not called like a method (t.fahrenheit()).


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9/5 + 32


t = Temperature(27)
print(t.fahrenheit)