#  Create a Student class with attributes name and marks. Add a method display() that prints the student's name and marks. Create 2 student objects and call display() on both.



class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"My name is {self.name}")
        print(f"{self.name} marks is {self.marks}")


s1 = Student("Abhinandan", 88)
s1.display()

s2 = Student("Abhishek", 90)
s2.display()


              