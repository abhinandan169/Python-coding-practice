# Given a string, find the first non-repeating character in it (a character that appears only once). Example: "swiss"


s = "swiss"
count = {}

for ch in s:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

for ch in s:
    if count[ch] == 1:
        print(ch)
        break        