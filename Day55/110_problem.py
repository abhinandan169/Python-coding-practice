# Given two strings, check if they are anagrams of each other (same letters, same count, different order). Print True or False.
# Example: "listen" and "silent"


s1 = "listen"
s2 = "silent"

if sorted(s1) == sorted(s2):
    print(True)
else:
    print(False)