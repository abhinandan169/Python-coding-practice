# Create a class Manager that inherits from Employee. Add a method show_department() that prints the protected _department attribute from inside the child class.


class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self._department = department
        self.__salary = salary

    def show_salary(self):
        print(self.__salary)

class Manager(Employee):
    def show_department(self):
        print(self._department)

m = Manager("Priya", "HR", 70000)
m.show_department()   