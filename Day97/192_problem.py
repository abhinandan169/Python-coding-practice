# Given a list of numbers, find the index of the largest number.[3, 9, 2, 7]


nums = [3, 9, 2, 7]
max_index = 0

for i in range(len(nums)):
    if nums[i] > nums[max_index]:
        max_index = i

print(max_index)