# Given a list of numbers, find the sum of all numbers divisible by 3.
# Example: [3, 5, 6, 9, 10, 12]

nums = [3, 5, 6, 9, 10, 12]

total = 0

for i in nums:
    if i % 3 == 0:
        total += i

print(total)