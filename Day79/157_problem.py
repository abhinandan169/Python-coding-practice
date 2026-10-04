# Given a string, count how many times each word appears, and print only the word(s) that appear the maximum number of times."the cat sat on the mat the cat ran"


sent = "the cat sat on the mat the cat ran"
words = sent.split()
count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)


max_count = max(count.values())

for word, c in count.items():
    if c == max_count:
        print(word)