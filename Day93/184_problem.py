# Given a list of numbers and a target number, remove all occurrences of the target and print the new list.[1, 2, 3, 2, 4, 2]


nums = [1, 2, 3, 2, 4, 2]
target = 2
result = []

for n in nums:
    if n != target:
        result.append(n)

print(result)