# Given the string "programming", count the frequency of each character and store it in a dictionary.


s = "programming"
count = {}

for char in s:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print(count)            