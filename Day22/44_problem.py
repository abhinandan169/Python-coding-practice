# Given a sentence, reverse each word individually but keep the word order same (without using slicing [::-1]).
# Example: "hello world"


sentence = "hello world"
words = sentence.split()
result = []


for word in words:
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    result.append(reversed_word)

final_sentence = " ".join(result)
print(final_sentence)