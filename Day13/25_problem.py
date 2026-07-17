#  Given the string "aabbbcccc", compress it by counting consecutive repeated characters — output should be "a2b3c4" (each character followed by its count). Use a loop.


s = "aabbbcccc"

result = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        result += s[i-1] + str(count)
        count = 1

result += s[-1] + str(count)

print(result)