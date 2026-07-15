# Write a function using recursion to find the sum of digits of a number (e.g., 1234 → 1+2+3+4 = 10).



def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        last_digits = n % 10
        remaining = n // 10
        return last_digits + sum_of_digits(remaining)
    

print(sum_of_digits(6644))    