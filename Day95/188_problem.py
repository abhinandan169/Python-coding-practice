# Given a list of numbers, find the average.[10, 20, 30, 40]


nums = [10, 20, 30, 40]
total = 0

for n in nums:
    total += n

average = total / len(nums)
print(average)