# Create a Student class with attributes name and marks (a list of numbers). Add a method average_marks() that returns the average of the marks list.


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average_marks(self):
        total = 0
        for m in self.marks:
            total += m
        avg = total / len(self.marks)
        return avg    
            
stu = Student("Abhinandan", [60, 74, 80, 88, 93])
print(stu.average_marks())
