# Given the string "Hello123World456", separate and print all the digits and all the alphabets separately using a loop.



s = "Hello123World456"

alphabets = ""
digits = ""

for char in s:
    if char.isalpha():
        alphabets += char
    elif char.isdigit():
        digits += char


print("alphabets:", alphabets)
print("digits:", digits)