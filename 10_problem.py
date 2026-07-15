# Given the list [10, 20, 30], take an index number as input from the user and print the value at that index. Handle the case of an invalid index using try-except.


nums = [10, 20, 30]

try:
    user = int(input())

    print(nums[user])

except IndexError:
    print("This Index is Invalid")