# Given a list of numbers, check if the list is sorted in ascending order. Print True or False.[1, 2, 3, 4, 5]


nums = [1, 2, 3, 4, 5]
is_sorted = True


for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        is_sorted = False

print(is_sorted) 