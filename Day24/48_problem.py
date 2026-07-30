# Create a parent class Animal with attribute name and a method speak() that prints "{name} makes a sound". Create a child class Dog that inherits from Animal, and override speak() to print "{name} barks". Create one object of each and call speak().


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} bark")


a = Animal("Cat")
a.speak()

d = Dog("Doggy Don")
d.speak()
