# Create a Student class with attributes name and marks. Add a method get_grade() that returns "A" if marks ≥ 90, "B" if marks ≥ 75, "C" if marks ≥ 40, else "Fail". Create a list of 4 students with different marks and print each one's name with their grade.



class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 40:
            return "C"
        else:
            return "Fail"

s1 = Student("A", 95)
s2 = Student("B", 80)
s3 = Student("C", 50)
s4 = Student("D", 30)

students = [s1, s2, s3, s4]

for student in students:
    print(f"{student.name}: {student.get_grade()}")