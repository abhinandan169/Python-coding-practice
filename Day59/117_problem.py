# Given a list of numbers, find all pairs of numbers that add up to a given target sum.
# Example: [2, 4, 3, 5, 7], target = 7

nums = [2, 4, 3, 5, 7]
target = 7

for i in range(len(nums)):

    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print([nums[i], nums[j]])   