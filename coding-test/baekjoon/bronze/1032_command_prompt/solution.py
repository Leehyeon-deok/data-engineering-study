n = int(input())
files = [input().strip() for _ in range(n)]

result = ""

for i in range(len(files[0])):
    ch = files[0][i]
    for j in range(1, n):
        if files[j][i] != ch:
            result += "?"
            break
    else:
        result += ch

print(result)
