# Given a sentence, find the word with the maximum number of vowels."I love programming in python"


sentence = "I love programming in python"
words = sentence.split()
vowels = "aeiouAEIOU"

max_word = words[0]
max_count = 0

for word in words:
    count = 0
    for ch in word:
        if ch in vowels:
            count += 1
    if count > max_count:
        max_count = count
        max_word = word

print(max_word) 