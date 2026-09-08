# Given a string, count the number of words in it that start with a vowel.
# Example: "An apple a day keeps doctor away"

words = "An apple a day keeps doctor away"

word_list = words.split()
count = 0


vowels = "aeiouAEIOU"

for word in word_list:
    if word[0] in vowels:
        count += 1

print(count)
