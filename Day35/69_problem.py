# Create an Employee class with attributes name and basic_salary. Add a method calculate_salary() that adds a fixed bonus of ₹5000 to the basic salary and returns the total. Create 2 employee objects and print their total salary.

class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
       return self.basic_salary + 5000


e1 = Employee("Abhinandan", 25000)
print(e1.calculate_salary())  

e2 = Employee("Avni", 50000)
print(e2.calculate_salary())