# Given the string "Abhinandan Kumar", count the number of vowels in it using a loop.


s = "Abhinandan Kumar"
count = 0

vowels = "aeiouAEIOU"

for char in s:
    if char in vowels:
        count += 1

print(count)
