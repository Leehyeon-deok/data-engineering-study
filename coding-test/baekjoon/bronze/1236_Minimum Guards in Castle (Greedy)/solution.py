N, M = map(int, input().split())
castle = [input() for _ in range(N)]

row = 0
col = 0

# 경비원 없는 행 찾기
for i in range(N):
    if 'X' not in castle[i]:
        row += 1

# 경비원 없는 열 찾기
for j in range(M):
    has_guard = False
    for i in range(N):
        if castle[i][j] == 'X':
            has_guard = True
            break
    if not has_guard:
        col += 1

print(max(row, col))
