# Given a list of numbers, find the sum of only the even numbers.
# Example: [1,2,3,4,5,6]


numbers = [1, 2, 3, 4, 5, 6]

total = 0

for num in numbers:
    if num % 2 == 0:
        total = total + num

print(total)