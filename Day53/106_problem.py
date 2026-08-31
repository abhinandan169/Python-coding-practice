# Given a string, check if it's a pangram or not — meaning it contains every letter of the alphabet at least once (ignore case). Print True or False.
# Example: "The quick brown fox jumps over the lazy dog"


s = "The quick brown fox jumps over the lazy dog"

s = s.lower()
unique_letters = set(s)
alphabet = set("abcdefghijklmnopqrstuvwxyz")

if alphabet.issubset(unique_letters):
    print(True)
else:
    print(False)
