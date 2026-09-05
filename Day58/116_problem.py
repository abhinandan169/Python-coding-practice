# Create a class Animal with attribute name and a method speak() that prints "<name> makes a sound". Create a class Dog that inherits from Animal and overrides speak() to print "<name> barks".

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "makes a sound")

class Dog(Animal):
    def speak(self):
        print(self.name, "barks")

d = Dog("Charlie")
d.speak()        