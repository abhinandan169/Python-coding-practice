# Given a list of numbers [1, 2, 2, 3, 4, 4, 4, 5], remove duplicates from it without using set(), and return a new list with only unique values (preserving order).


nums_of_list = [1, 2, 2, 3, 4, 4, 4, 5]
num_list = []

for i in nums_of_list:
    if i not in num_list:
        num_list.append(i)       

print(num_list)