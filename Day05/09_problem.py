# Create an Employee parent class with a salary attribute and a show_salary() method. Create a Manager child class with an extra bonus attribute and a total_salary() method that returns salary + bonus.


class Employee:
    def __init__(self, salary):
        self.salary = salary

    def show_salary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, salary, extrabonus):
        super().__init__(salary)
        self.extrabonus = extrabonus

    def total_salary(self):
        return self.salary + self.extrabonus

m = Manager(60000 , 7000)
print(m.show_salary())
print(m.total_salary())   