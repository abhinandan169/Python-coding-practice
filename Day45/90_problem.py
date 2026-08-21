# Given a list of words, group them into a dictionary where the key is the word length and the value is a list of words with that length.
# Example: ["cat", "dog", "apple", "bat", "banana"]


words = ["cat", "dog", "apple", "bat", "banana"]
result = {}   

for word in words:
    length = len(word)          
    
    if length in result:           
        result[length].append(word) 
    else:
        result[length] = [word]

print(result)