# Given a list of numbers, find all numbers that are perfect squares.[1, 2, 4, 5, 9, 10, 16]


import math

nums = [1, 2, 4, 5, 9, 10, 16]
result = []

for num in nums:
    root = math.sqrt(num)
    if root == int(root):
        result.append(num)

print(result)