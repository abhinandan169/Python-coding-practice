# Create a class Animal with attribute name. Create a class Zoo that stores a list of Animal objects. Add a method find_animal(name) using the duck-typing style loop, and also add a __len__ to Zoo that returns the number of animals.


class Animal:
    def __init__(self, name):
        self.name = name

class Zoo:
    def __init__(self):
        self.list_animal = []

    def find_animal(self, name):
        for animal in self.list_animal:
            if animal.name == name:
                print(animal.name)
                return
        print("Not Found")

    def __len__(self):
        return len(self.list_animal) 
           

z = Zoo()
z.list_animal.append(Animal("Lion"))
z.list_animal.append(Animal("Tiger"))

z.find_animal("Tiger")
z.find_animal("Elephant")
print(len(z))
