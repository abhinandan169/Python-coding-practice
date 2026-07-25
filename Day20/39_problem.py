# Given a list of numbers, remove duplicates while preserving the original order (without using set()).
# Example: [1,2,2,3,4,4,5] → [1,2,3,4,5]



num_list = [1, 2, 2, 3, 4, 4, 5]
num = []

for i in num_list:
    if i not in num:
        num.append(i)

print(num)