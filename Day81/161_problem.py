# Given a string, remove all duplicate characters, keeping only the first occurrence of each."programming"

s = "programming"
seen = {}
result = ""

for ch in s:
    if ch not in seen:
        result += ch
        seen[ch] = True

print(result)