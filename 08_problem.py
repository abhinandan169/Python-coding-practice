# Given the dictionary {"Python": 85, "DSA": 70, "SQL": 60}, print each subject with its marks, and also find which subject has the highest marks.


marks = {
    "Python" : 85,
    "DSA" : 70,
    "SQL" : 60
        }

for i  in marks:
    print(i, marks[i])


highest_subject = ""   
highest_marks = 0

for i in marks:
    if marks[i] > highest_marks:
        highest_marks = marks[i]
        highest_subject = i

print("Highest", highest_subject, highest_marks)