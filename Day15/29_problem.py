# Given a list of numbers [23, 45, 12, 67, 34, 89, 21], find the sum of the largest and smallest number in the list, using a loop.


nums = [23, 45, 12, 67, 34, 89, 21]

largest = nums[0]
smallest = nums[0]

for i in nums:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print("Largest:", largest)
print("Smallest:", smallest)

total = largest + smallest
print("sum:", total)