# Given a list of numbers, find the maximum difference between any two elements such that the smaller element comes before the larger one. Example: [7, 1, 5, 3, 6, 4]


nums = [7, 1, 5, 3, 6, 4]

min_so_far = nums[0]
max_diff = 0

for i in nums:
    if i - min_so_far > max_diff:
        max_diff = i - min_so_far
    if i < min_so_far:
        min_so_far = i

print(max_diff)