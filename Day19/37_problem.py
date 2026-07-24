# Given a sentence, count how many times each word appears (use a dictionary).
# Example: "the cat sat on the mat the cat ran"


sentence = "the cat sat on the mat the cat ran"
words = sentence.split()
count = {}

for word in words:
    if word in count:
        count[word] = 1
    else:
        count[word] = 1

print(count)                 