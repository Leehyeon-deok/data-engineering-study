N = int(input())

# 빠진 조건
if N == 0:
    print("NO")
    exit()

facts = []
f = 1
i = 0

while f <= N:
    facts.append(f)
    i += 1
    f *= i

facts.reverse()

used = 0

for x in facts:
    if N >= x:
        N -= x
        used += 1

print("YES" if N == 0 and used > 0 else "NO")
