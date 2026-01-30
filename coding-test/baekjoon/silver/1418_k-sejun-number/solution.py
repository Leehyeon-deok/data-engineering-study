N = int(input())
K = int(input())

# 1. 가장 작은 소인수(spf) 배열 만들기
spf = [0] * (N + 1)
for i in range(2, N + 1):
    if spf[i] == 0:          # i는 소수
        for j in range(i, N + 1, i):
            if spf[j] == 0:
                spf[j] = i

# 2. K-세준수 개수 세기
count = 0
for i in range(1, N + 1):
    x = i
    is_valid = True

    while x > 1:
        if spf[x] > K:
            is_valid = False
            break
        x //= spf[x]

    if is_valid:
        count += 1

print(count)
