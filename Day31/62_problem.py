# Create a Student class with attribute name. Use a class variable all_students (an empty list) that automatically stores every student object created (add it inside __init__). Add a class method total_students() that prints how many students exist. Create 3 students, then call total_students().

class Student:
    all_students = []

    def __init__(self, name):
        self.name = name
        Student.all_students.append(self)

    @classmethod
    def total_students(cls):
        print(f"Total Students: {len(cls.all_students)}")



s1 = Student("Abhinandan")
s2 = Student("Laxmi")
s3 = Student("Rajeshwari")

Student.total_students() 


