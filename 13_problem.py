# Given the dictionary {"Rahul": 85, "Priya": 92, "Aman": 78}, print the names of students who scored more than 90 marks.


marks = {"Rahul": 85, "Priya": 92, "Aman": 78}

for i in marks:
    if marks[i] > 90:
        print(i, marks[i])
     
