# Given a string, reverse the order of words (not characters)."I love Python"


words = "I Love Python"

word_list = words.split()
reversed_list = word_list[::-1]
result = " ".join(reversed_list)

print(result)