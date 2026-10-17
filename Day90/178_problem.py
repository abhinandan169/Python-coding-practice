# Create a class Student with a class variable school = "ABC School" and an instance variable name. Create two objects. Change the school for only the first object (s1.school = "XYZ School") and show that the second object and the class itself still have the old value.


class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

s1 = Student("Rahul")
s2 = Student("Priya")

print(s1.school, s2.school) 

s1.school = "XYZ School"

print(s1.school)             
print(s2.school)              
print(Student.school)         