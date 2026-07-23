# Given a string, count the total number of vowels (a, e, i, o, u) in it (case-insensitive).
# Example: "Hello World" → 3 (e, o, o)


s = "Hello World"
count = 0
vowels = "aeiouAEIOU"


for char in s:
    if char in vowels:
        count += 1

print("Vowels:", count)     