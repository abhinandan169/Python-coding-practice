# Create an Employee class with a class variable company (set to "TechCorp"). Add a class method change_company(cls, new_name) (using @classmethod) that updates the company for all objects. Create 2 employee objects, print their company, then change it and print again for both.


class Employee:
    company = "TechCorp"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name



e1 = Employee("Abhinandan")
e2 = Employee("Abhishek")


print(e1.company)
print(e2.company)

Employee.change_company("TechVista")

print(e1.company)
print(e2.company)