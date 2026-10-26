# Given a string, check if it has no uppercase letters, without using .islower(). Print True or False. "hello world"


s = "hello world"
no_upper = True

for ch in s:
    if ch.isupper():
        no_upper = False

print(no_upper)