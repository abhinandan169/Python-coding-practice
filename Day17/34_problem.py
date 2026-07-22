# Given a list of numbers = [12, 45, 2, 41, 31, 10, 8, 6, 4], find the second largest number without using sorted() or max() — use a loop.


numbers = [12, 45, 2, 41, 31, 10, 8, 6, 4]

largest = numbers[0]
second_largest = float('-inf')

for i in numbers:
    if i > largest:
        second_largest = largest
        largest = i  
    elif i > second_largest and i != largest:
        second_largest = i

print("Largest:", largest)
print("Second Largest:", second_largest)     
