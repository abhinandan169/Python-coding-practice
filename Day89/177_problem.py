# Given a string, find the number of characters that are not letters (spaces, digits, symbols)."Hi 5 there!"


s = "Hi 5 there!"
count = 0

for ch in s:
    if not ch.isalpha():
        count += 1

print(count)