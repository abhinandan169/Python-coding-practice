# Given a string, count how many times each character appears (use a dictionary).
# Example: "hello" → {'h':1, 'e':1, 'l':2, 'o':1}


character_str = "hello"
count = {}


for char in character_str:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print(count)