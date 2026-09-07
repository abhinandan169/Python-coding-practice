# Create a class Student with a private attribute __marks (use double underscore). Add a method set_marks(marks) that only allows setting marks if it's between 0 and 100 (otherwise print "Invalid marks"), and a method get_marks() that returns the marks


class Student:
    def __init__(self):
        self.__marks = 0

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")

    def get_marks(self):
        return self.__marks

s = Student()
s.set_marks(80)
s.set_marks(130)
print(s.get_marks())                    