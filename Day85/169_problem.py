# Given a string, count how many words have more than 3 letters."I love to code in Python"


s = "I love to code in Python"
count = 0

for word in s.split():
    if len(word) > 3:
        count += 1

print(count)