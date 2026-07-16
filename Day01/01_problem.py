# Take a string as user input and check whether it is a palindrome or not.


a = input("Enter a string")

if a == (a[::-1]):
    print("This is a palindrome")

else:
    print("This is not a palindrome")    