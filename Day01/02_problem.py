# Given the list [5, 2, 8, 1, 9, 3], find the largest and smallest number using a loop (without using max()/min()).


num = [5, 2, 8, 1, 9, 3]
biggest = num[0]
smallest = num[0]

for i in num:
    if i > biggest:
        biggest = i
    if i < smallest:
        smallest = i

print("biggest", biggest)
print("smallest", smallest)        