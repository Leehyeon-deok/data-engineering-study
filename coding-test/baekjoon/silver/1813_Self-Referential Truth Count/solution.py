N = int(input())
arr = list(map(int, input().split()))

answer = -1

for x in range(N + 1):
    if arr.count(x) == x:
        answer = max(answer, x)

print(answer)
