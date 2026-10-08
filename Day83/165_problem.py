# Given a string, replace all spaces with underscores without using .replace()."hello world today"

s = "hello world today"
result = ""

for ch in s:
    if ch == " ":
        result += "_"
    else:
        result += ch

print(result)