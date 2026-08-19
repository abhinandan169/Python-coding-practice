# Create a Person class with attributes name and age. Create a list of 5 Person objects. Write a loop to find and print the name of the youngest person (comparison logic, no min()).


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Abhinandan", 20)
p2 = Person("Martin", 26)
p3 = Person("Mariana", 32)
p4 = Person("Avni", 19)
p5 = Person("Leaon", 28)

people = [p1, p2, p3,  p4, p5]

youngest = people[0]

for person in people:
    if person.age < youngest.age:
        youngest = person

print(youngest.name)        