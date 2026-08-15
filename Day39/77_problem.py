# Create an Employee class with attributes name and days_present (out of 30 working days). Add a method attendance_percent() that returns (days_present / 30) * 100. Create a list of 3 employees and print each one's attendance percentage.

class Employee:
    def __init__(self, name, days_present):
        self.name = name
        self.days_present = days_present

    def attendance_percent(self):
        return (self.days_present / 30) * 100

e1 = Employee("Abhinandan", 28)
e2 = Employee("Rohan", 20)
e3 = Employee("Alex", 30)


employees = [e1, e2, e3]

for emp in employees:
    print(f"{emp.name}: {emp.attendance_percent()}%")