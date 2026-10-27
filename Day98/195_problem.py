# Using the same Student class (with __lt__ and a __repr__ so the output is readable), create a list of 3 students and sort it with sorted(). Print the sorted list.


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __lt__(self, other):
        return self.marks < other.marks

    def __repr__(self):
        return f"Student({self.name}, {self.marks})"

students = [
    Student("Rahul", 70),
    Student("Priya", 85),
    Student("Aman", 60),
]

print(sorted(students))