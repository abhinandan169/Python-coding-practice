# Create a class Quiz that stores questions and their answers as a dictionary. Add a method check_answer(question, answer) that returns True if the given answer matches the stored answer for that question, otherwise False.


class Quiz:
    def __init__(self):
        self.Quiz_data = {"2+2": "4", "Capital of India": "New Delhi"}

    def check_answer(self, question, answer):
        return self.Quiz_data[question] == answer

q = Quiz()
print(q.check_answer("2+2", "4"))
print(q.check_answer("Capital of India", "New Delhi"))      