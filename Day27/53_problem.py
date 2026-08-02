# Create a Calculator class with a static method add(a, b) that returns a + b, and another static method multiply(a, b) that returns a * b. Call both methods without creating an object (directly using the class name).


class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


print(Calculator.add(6, 4))
print(Calculator.multiply(5, 4))