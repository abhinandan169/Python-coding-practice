# Given a string, check if it's a valid palindrome ignoring spaces, punctuation, and case. "A man a plan a canal Panama"


s = "A man a plan a canal Panama"
s = s.lower()

cleaned = ""
for ch in s:
    if ch.isalpha():
        cleaned += ch

if cleaned == cleaned[::-1]:
    print(True)
else:
    print(False)