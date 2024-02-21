def is_palindrome(s):
    return s == s[::-1]

n = int(input())
strings = []
for i in range(n):
    strings.append(input())

pairs = []
for i in range(n):
    for j in range(i+1, n):
        if is_palindrome(strings[i] + strings[j]):
            pairs.append((i+1, j+1))

for pair in pairs:
    print(pair[0], pair[1])

