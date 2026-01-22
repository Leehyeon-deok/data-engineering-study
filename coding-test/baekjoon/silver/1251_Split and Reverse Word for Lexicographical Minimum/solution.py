word = input().strip()
n = len(word)

result = []

for i in range(1, n - 1):
    for j in range(i + 1, n):
        a = word[:i][::-1]
        b = word[i:j][::-1]
        c = word[j:][::-1]
        result.append(a + b + c)

print(min(result))
