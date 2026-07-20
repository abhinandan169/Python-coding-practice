# Given the string "racecar level", check whether each word in the sentence is a palindrome or not, and print the result for each word separately.


s = "racecar level"
words = s.split()

for word in words:
    if word == word[::-1]:
        print(word, "is a palindrome")
    else:
        print(word, "is not a palindrome")     