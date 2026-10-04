# Given a list of numbers, find the second largest number without using sorted() or max().[10, 5, 20, 8, 20, 15]

nums = [10, 5, 20, 8, 20, 15]

largest = nums[0]
second_largest = float('-inf')

for i in nums:
    if i > largest:
        second_largest = largest
        largest = i

    elif i > second_largest and i != largest:
        second_largest = i

print("Largest", largest)
print("Second Largest", second_largest)            
