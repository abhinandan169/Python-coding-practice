# Create a Student class with attributes name and marks. Create a list of 3 Student objects. Write a loop to calculate and print the total marks of all students combined (simple sum, no comparison needed).


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("Abhinandan", 77)
s2 = Student("Deepanshi", 89)
s3 = Student("Anushka", 92)

students = [s1, s2, s3]
total = 0

for student in students:
    total = total + student.marks

 
print("Total all Students Marks is:", total)        
