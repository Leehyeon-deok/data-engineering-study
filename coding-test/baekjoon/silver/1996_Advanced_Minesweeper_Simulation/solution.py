import sys
input = sys.stdin.readline

N = int(input())
board = [list(input().strip()) for _ in range(N)]

# 8방향
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1,  0,  1, -1, 1, -1, 0, 1]

result = [[''] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        # 지뢰가 있는 칸
        if board[i][j] != '.':
            result[i][j] = '*'
        else:
            mine_count = 0
            for d in range(8):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < N and 0 <= ny < N:
                    if board[nx][ny] != '.':
                        mine_count += int(board[nx][ny])
            
            if mine_count >= 10:
                result[i][j] = 'M'
            else:
                result[i][j] = str(mine_count)

# 출력
for row in result:
    print(''.join(row))
