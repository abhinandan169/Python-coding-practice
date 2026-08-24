# Given a sentence, find and print the longest word in it.
# Example: "I love Python programming"

sent = "I Love Python Programming"

longest = " "

for word in sent.split():
    if len(word) > len(longest):
        longest = word

print("Longest Word:", longest)        