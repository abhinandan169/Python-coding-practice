# Given a string, check if it contains only digits. Print True or False.
# Example: "12345"


# First Approach

s = "12345"

all_digits = True

for ch in s:
    if not ch.isdigit():
        all_digits = False

print(all_digits)


# Second Approach


s = "12a45"

all_digits = True

for ch in s:
    if not ch.isdigit():
        all_digits = False

print(all_digits)        