# Given a list containing numbers from 1 to n with one number missing, find the missing number.
# Example: [1,2,4,5,6] (n=6)


num_list = [1, 2, 4, 5, 6]
n = len(num_list) + 1

expected_sum = n * (n+1) // 2
actual_sum = sum(num_list)


missing_number = expected_sum - actual_sum

print("Missing number:", missing_number)
