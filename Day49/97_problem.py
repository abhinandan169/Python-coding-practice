# Given a list of numbers, find the second smallest number in it.
# Example: [5, 1, 9, 1, 3]


nums = [5, 1, 9, 1, 3]

smallest = nums[0]
second_smallest = float('inf')

for i in nums:
    if i < smallest:
        second_smallest = smallest
        smallest = i

    elif i < second_smallest and i != smallest:
        second_smallest = i

print("Second Smallest :", second_smallest)