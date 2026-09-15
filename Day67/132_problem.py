# Given a list of numbers, find all numbers that appear more than once (duplicates).
# [1, 2, 3, 2, 4, 1, 5]


nums = [1, 2, 3, 2, 4, 1, 5]
count = {}

for i in nums:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print(count)             

result = []

for key, value in count.items():
    if value > 1:
        result.append(key)

print(result)        