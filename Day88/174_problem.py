# Create a class Employee with a public attribute name, a protected attribute _department, and a private attribute __salary. Add a method show_salary() that prints the salary. Create an object, print name and _department directly, and call show_salary().


class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self._department = department
        self.__salary = salary

    def show_salary(self):
        print(self.__salary)

e = Employee("Rahul", "IT", 50000)
print(e.name)
print(e._department)   
e.show_salary()         