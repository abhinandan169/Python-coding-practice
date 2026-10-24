# Given a string and a character, find the index of the first occurrence of that character without using .find() or .index(). If it is not present, print -1.



s = "hello"
target = "l"
position = -1

for i in range(len(s)):
    if s[i] == target:
        position = i
        break

print(position)