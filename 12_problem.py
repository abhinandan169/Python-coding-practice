# Given the list [4, 8, 15, 16, 23, 42], create a new list containing only the even numbers, using a loop.



nums = [4, 8, 15, 16, 23, 42]
even_list = []

for i  in nums:
    if i % 2 == 0:
        even_list.append(i)

print(even_list)         