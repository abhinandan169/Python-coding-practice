# Given a list of numbers, separate them into two lists — one for even numbers and one for odd numbers.
# Example: [1, 2, 3, 4, 5, 6]

nums = [1, 2, 3, 4, 5, 6]

even = []
odd = []

for i in nums:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)


print("Even :", even)
print("Odd :", odd)
            