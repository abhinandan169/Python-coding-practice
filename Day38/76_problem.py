# Create a Student class with attributes name and marks. Create a list of 4 Student objects. Write a loop to calculate and print the average marks of all students.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("Abhinandan", 60)
s2 = Student("Ranidurgawati", 90)
s3 = Student("Annapurna", 87)
s4 = Student("Abhimanu", 68)

students = [s1, s2, s3, s4]
total = 0

for student in students:
    total = total + student.marks

average = total / len(students)

print("The Average marks of all students", average)    