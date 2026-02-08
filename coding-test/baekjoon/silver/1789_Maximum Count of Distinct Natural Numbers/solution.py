S = int(input())

total = 0
n = 0

while total + (n + 1) <= S:
    n += 1
    total += n

print(n)
