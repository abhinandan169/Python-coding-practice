# Given a string, remove all the vowels from it and print the result.
# Example: "Hello World"

words = "Hello World"

result = ""
vowels = "aeiouAEIOU"

for i in words:
    if i not in vowels:
        result += i

print(result)