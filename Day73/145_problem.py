# Given a string, find the length of the longest word."I love Python programming"


sent = "I Love Python Programming"
longest = " "

for word in sent.split():
    if len(word) > len(longest):
        longest = word

print("Longest Word:", longest)
print(len(longest)) 