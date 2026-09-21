#  Given a list of numbers, move all zeros to the end while keeping the order of non-zero elements.[0, 1, 0, 3, 12]


nums = [0, 1, 0, 3, 12]

non_zero = []
zero_count = 0

for i in nums:
    if i != 0:
        non_zero.append(i)
    else:
        zero_count += 1

result = non_zero + [0] * zero_count
print(result)