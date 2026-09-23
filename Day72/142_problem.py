# Create a class Greet with a method hello(name=None) that prints "Hello!" if no name is given, otherwise prints "Hello, <name>!".

class Greet:
    def hello(self, name=None):
        if name == None:
            print("Hello!")

        else:
            print(f"Hello, {name}!")

g = Greet()
g.hello()
g.hello("Abhi")                