# Given a list of numbers and a target number, count how many times the target appears in the list. [1, 2, 3, 2, 4, 2]


nums = [1, 2, 3, 2, 4, 2]
target = 2
count = 0

for n in nums:
    if n == target:
        count += 1

print(count)