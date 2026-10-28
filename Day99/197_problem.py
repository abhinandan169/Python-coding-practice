# Given a string, count how many words end with the letter "s"."cats dogs bird fish"


s = "cats dogs bird fish"
count = 0

for word in s.split():
    if word[-1] == "s":
        count += 1

print(count)