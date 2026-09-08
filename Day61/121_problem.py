# Given a list of numbers, rotate the list to the right by one position.
# Example: [1, 2, 3, 4, 5]

nums = [1, 2, 3, 4, 5]

last = nums[-1]

rest = nums[:-1]

result = [last] + rest
print(result)