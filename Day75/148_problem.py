# Given a list of numbers, replace every negative number with 0.[1, -2, 3, -4, 5]

nums = [1, -2, 3, -4, 5]

for i in range(len(nums)):
    if nums[i] < 0:
        nums[i] = 0    

print(nums)