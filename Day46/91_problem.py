# Given a sentence, count how many words it has (use .split(), then count the items).
# Example: "I love Python programming"


sentence = "I Love Python Programming"

words = sentence.split()
count = 0

for word in words:
        count += 1


print(count)
