N, L, D = map(int, input().split())

total_time = N * L + (N - 1) * 5

t = 0
while True:
    if t >= total_time:
        print(t)
        break

    cycle = t // (L + 5)
    position = t % (L + 5)

    if cycle < N and position < L:
        # 노래 중
        t += D
    else:
        # 조용한 구간
        print(t)
        break
