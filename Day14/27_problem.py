# Given the string "Hello World", count how many times each word appears if the sentence is "the cat sat on the mat and the cat ran" — print the word that occurs the most, using a dictionary.


s = "the cat sat on the mat and the cat ran"
words = s.split()
count = {}


for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1   

print(count)


highest_word = ""
highest_count = 0

for word in count:
    if count[word] > highest_count:
        highest_count = count[word]
        highest_word = word

print("Highest_word:", highest_word, highest_count)