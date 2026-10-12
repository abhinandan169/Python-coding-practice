# Given a list of numbers, find the sum of all numbers at even indexes (0, 2, 4, ...).[10, 20, 30, 40, 50]


nums = [10, 20, 30, 40, 50]
total = 0

for i in range(len(nums)):
    if i % 2 == 0:
        total += nums[i]

print(total)