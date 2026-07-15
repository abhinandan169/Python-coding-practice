# Given the list [10, 25, 3, 47, 8, 19], find the second largest number using a loop, without using sort().


nums = [10, 25, 3, 47, 8, 19]

largest = float('-inf')
second_largest = float('-inf')

for i in nums:
    if i > largest:
        second_largest = largest    
        largest = i                 
    elif i > second_largest and i != largest:
        second_largest = i

print(second_largest)