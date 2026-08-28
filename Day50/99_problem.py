# Create a class Employee with attributes name and salary. Add a method give_raise(amount) that increases the salary by that amount and prints the new salary.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary = self.salary + amount
        print(self.salary)


e = Employee("Abhinandan", 40000)
e.give_raise(5000)     

            