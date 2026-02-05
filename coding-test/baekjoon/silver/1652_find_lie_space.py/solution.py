N = int(input())
room = [input().strip() for _ in range(N)]

horizontal = 0
vertical = 0

# 가로 검사
for row in room:
    count = 0
    for c in row:
        if c == '.':
            count += 1
        else:
            if count >= 2:
                horizontal += 1
            count = 0
    if count >= 2:
        horizontal += 1

# 세로 검사
for col in range(N):
    count = 0
    for row in range(N):
        if room[row][col] == '.':
            count += 1
        else:
            if count >= 2:
                vertical += 1
            count = 0
    if count >= 2:
        vertical += 1

print(horizontal, vertical)
