# Given a string, check if every opening bracket ( has a matching closing bracket ) (balanced brackets)."(a+b)*(c-d)"

brac_string = "(a+b)*(c-d)"

counter = 0

for count in brac_string:
    if count == "(":
        counter += 1
    elif count == ")":
        counter -= 1

if counter == 0:
    print(True)
else:
    print(False)    

print(counter)            