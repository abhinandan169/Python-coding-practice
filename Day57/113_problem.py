# Given a list of numbers, find the frequency of the most frequent number (i.e., how many times the most common number appears).
# Example: [1, 3, 2, 3, 4, 3, 2]


num_of_list = [1, 3, 2, 3, 4, 3, 2]

freq = {}

for i in num_of_list:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(max(freq.values()))            