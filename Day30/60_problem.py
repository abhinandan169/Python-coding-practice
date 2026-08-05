# Create a Person class with attributes name and age. Create a list of 4 Person objects with different ages. Write a loop to find and print the name of the oldest person (without using max() — use comparison logic like you did in "Second Largest Number" on Day 17).


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Abhinandan", 21)
p2 = Person("Abhishek", 22)
p3 = Person("Arijit", 35)
p4 = Person("Suhani", 19)
p5 = Person("Avnii", 20)

people = [p1, p2, p3,  p4, p5]

oldest = people[0]


for person in people:
    if person.age > oldest.age:
        oldest = person

print("Name = ", oldest.name, "Age =", oldest.age)

          