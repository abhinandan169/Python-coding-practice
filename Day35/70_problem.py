# Create a Student class with attributes name and marks. Create a list of 5 Student objects with different marks. Write a loop to count and print how many students passed (marks ≥ 40).

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


s1 = Student("Abhinandan", 39)
s2 = Student("Avni", 80)
s3 = Student("Anushka", 92)
s4 = Student("Abhishek", 59)
s5 = Student("Deepanshi", 77)


students = [s1, s2, s3, s4, s5]
count = 0

for student in students:
    if student.marks >= 40:
        count +=  1

print("Total Passed Students:", count)