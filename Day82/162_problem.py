# Create a class Classroom with attribute students (a list). Add __len__ so that len(classroom_obj) returns the number of students.


class Classroom:
    def __init__(self, students):
        self.students = students

    def __len__(self):
        return len(self.students)

c = Classroom(["A", "B", "C"])
print(len(c))        