def is_palindrome(s):
    return s == s[::-1]

n = int(input())
strings = []
for _ in range(n): #здесь просто получаем ввод строк
    strings.append(input())

pairs = []
for i in range(n):
    for j in range(i+1, n):
        if is_palindrome(strings[i] + strings[j]):
            pairs.append((i+1, j+1))
        if is_palindrome(strings[j] + strings[i]):
            pairs.append((j+1, i+1))

pairs.sort()  # Сортируем пары по возрастанию индексов

for pair in pairs:
    print(pair[0], pair[1])
