# Given a number, find the sum of its digits using a loop (without converting to string).
# Example: 1234 → 10 (1+2+3+4)


n = 1234
total = 0

while n > 0:
    total += n % 10
    n = n // 10

print(total)    