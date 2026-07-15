# Given the list [12, 45, 7, 23, 56, 89, 34], find the average of the numbers using a loop.



nums = [12, 45, 7, 23, 56, 89, 34]
total = 0

for i in nums:
    total += i


count = len(nums)
average = total / count

print(average)