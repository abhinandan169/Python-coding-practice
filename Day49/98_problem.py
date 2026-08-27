# Given a string, count how many uppercase letters and how many lowercase letters it has.
# Example: "Hello World"


string = "Hello World"

uppercase_count = 0
lowercase_count = 0

for i in string:
    if i.isupper():
        uppercase_count += 1
    else:
        lowercase_count += 1

print("Uppercase:", uppercase_count)
print("Lowercase:", lowercase_count) 