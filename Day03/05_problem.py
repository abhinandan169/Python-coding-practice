# Write a function that divides two numbers. Handle the case where the divisor is zero using try-except, and print an appropriate message.


def divide(a , b):
    try:
        result = a / b
        print("Result", result)
        
    except ZeroDivisionError:
        print("cannot divided by Zero")

divide(10, 2)
divide(5,0)             