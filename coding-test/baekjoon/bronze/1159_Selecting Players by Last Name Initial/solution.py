import sys

n = int(sys.stdin.readline())
count = {}

for _ in range(n):
    name = sys.stdin.readline().strip()
    first = name[0]
    count[first] = count.get(first, 0) + 1

result = []

for key in count:
    if count[key] >= 5:
        result.append(key)

if len(result) == 0:
    print("PREDAJA")
else:
    result.sort()
    print("".join(result))
