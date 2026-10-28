# Given a list of numbers, find the largest number without using max().[4, 9, 2, 7]


nums = [4, 9, 2, 7]
largest = nums[0]

for n in nums:
    if n > largest:
        largest = n

print(largest)