# Given a string, check if it contains at least one digit. Print True or False."hello123"


s = "hello123"
has_digit = False

for ch in s:
    if ch.isdigit():
        has_digit = True

print(has_digit)