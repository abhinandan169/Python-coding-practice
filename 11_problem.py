# Given the sentence "the quick brown fox jumps", count the number of words in it by counting spaces (without using split() or len() on a list).



words = "the quick brown fox jumps"
count = 0


for char in words:
    if char == " ":
        count += 1

print(count + 1)               
        