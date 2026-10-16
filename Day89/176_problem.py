# Given a list of numbers, find how many numbers are greater than 10. [5, 12, 8, 20, 15, 3]


nums = [5, 12, 8, 20, 15, 3]
count = 0

for n in nums:
    if n > 10:
        count += 1

print(count)