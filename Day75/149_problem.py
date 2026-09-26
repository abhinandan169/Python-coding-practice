# Given two strings, check if one is a rotation of the other."waterbottle"


s1 = "waterbottle"
s2 = "erbottlewat"

double = s1 + s1

if s2 in double:
    print(True)
else:
    print(False)
