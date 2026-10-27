# Create a class Student with attributes name and marks. Add __lt__ so that one student is “less than” another if their marks are lower. Compare two students with <.


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __lt__(self, other):
        return self.marks < other.marks

s1 = Student("Rahul", 70)
s2 = Student("Priya", 85)

print(s1 < s2) 
print(s2 < s1)    