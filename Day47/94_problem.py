# Given a list of numbers, count how many are positive, how many are negative, and how many are zero.
# Example: [5, -3, 0, 8, -1, 0]


nums = [5, -3, 0, 8, -1, 0]

positive = 0
negative = 0
zero = 0

for i in nums:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
    else:
        zero += 1        

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)                 
