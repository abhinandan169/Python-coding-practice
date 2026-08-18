# Create a Person class with attributes name and age. Add a method category() that returns "Child" if age < 13, "Teenager" if age < 20, "Adult" if age < 60, else "Senior Citizen". Create a list of 4 people with different ages and print each one's name with their category.

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def category(self):
        if self.age < 13:
            return "Child"
        elif self.age < 20:
            return "Teenager"
        elif self.age < 60:
            return "Adult"
        else:
            return "Senior citizen"

p1 = Person("Amit", 10)
p2 = Person("Abhinandan", 19)
p3 = Person("Mayawati", 17)
p4 = Person("Rahul", 55)


people = [p1, p2, p3, p4]

for person in people:
    print(f"{person.name}: {person.category()}")
          