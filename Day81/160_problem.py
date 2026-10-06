# Given a list of numbers, find the median (middle value when sorted).[7, 1, 3, 9, 5]

nums = [7, 1, 3, 9, 5]
nums.sort()

n = len(nums)
median = nums[n // 2]

print(median)