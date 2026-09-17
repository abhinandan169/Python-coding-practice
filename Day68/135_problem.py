# Create a class Employee with attributes name, salary. Add a class method from_string(data) that takes a string like "Rahul,50000" and returns a new Employee object (split the string, convert salary to int).


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, data):
        parts = data.split(",")
        name = parts[0]
        salary = int(parts[1])
        return cls(name, salary)

e = Employee.from_string("Rahul,50000")
print(e.name, e.salary)
