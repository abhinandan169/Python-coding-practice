# Given a list of numbers, find the index of the first number that is greater than a given value.
# Example: [3, 7, 1, 9, 4], value = 5 → index 1 (number 7 is the first one greater than 5)


num_of_list = [3, 7, 1, 9, 4]
value = 5

for i in range(len(num_of_list)):
    if num_of_list[i] > value:
        print(i)
        break