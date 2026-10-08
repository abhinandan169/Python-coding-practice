# Given a list of numbers, create a new list containing the square of each number.[1, 2, 3, 4]


nums = [1, 2, 3, 4]
squares = []

for n in nums:
    squares.append(n * n)

print(squares)