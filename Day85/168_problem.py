# Given a list of numbers, print the numbers that are greater than the average of the list.[10, 20, 30, 40, 50]


nums = [10, 20, 30, 40, 50]

average = sum(nums) / len(nums)
result = []

for n in nums:
    if n > average:
        result.append(n)

print(result)