# Given the string "Programming", reverse it manually using a loop, without using slicing ([::-1]) or any built-in reverse function.



s = "Programming"

reversed_str = ""

for char in s:
    reversed_str = char + reversed_str

print(reversed_str)    


