# Given the list [3, 6, 7, 9, 10, 12], find the sum of all numbers divisible by 3, using a loop.


num = [3, 6, 7, 9, 10, 12]
total = 0

for i in num:
    if i % 3 == 0:
        total += i

print(total) 


