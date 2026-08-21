# Given two numbers start and end, print all prime numbers between them (a prime number is only divisible by 1 and itself; use nested loops, no built-in prime-check library).
# Example: start=10, end=20 → 11, 13, 17, 19


start = 10
end = 20

for num in range(start, end+1):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)    