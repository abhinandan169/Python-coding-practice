# Given a string, capitalize the first letter of every word (title case), without using the built-in .title() method.
# Example: "hello world from python"

s = "hello world from python"
words = s.split()

result = []
for word in words:
    new_word = word[0].upper() + word[1:]
    result.append(new_word)


final = " ".join(result)
print(final)