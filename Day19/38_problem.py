# Given a string, check whether it is a palindrome or not (same forward and backward), without using slicing ([::-1]) or built-in reverse functions — use a loop.
# Example: "madam" → True, "hello" → False



s = "madam"
reversed_s = ""

for char in s:
    reversed_s = char + reversed_s

if s == reversed_s:
    print("This is a palindrome")
else:
    print("This is not a palindrome")



h = "hello"
reversed_h = ""

for char in h:
    reversed_h = char + reversed_h

if h == reversed_h:
    print("This is a palindrome")
else:
    print("This is not a palindrome")
         