# Given a string, check if it's a valid identifier — meaning it starts with a letter or underscore, and contains only letters, digits, or underscores (no spaces or special characters).
# Example: "my_var1"


s = "my_var1"
print(s.isidentifier())

s = "1var"
print(s.isidentifier())


s = "my var"
print(s.isidentifier())