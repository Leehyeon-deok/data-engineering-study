board = input().strip()
result = ""
i = 0

while i < len(board):
    if board[i] == 'X':
        count = 0
        # 연속된 X 길이 세기
        while i < len(board) and board[i] == 'X':
            count += 1
            i += 1

        # 홀수면 불가능
        if count % 2 != 0:
            print(-1)
            exit()

        # AAAA 먼저 채우기
        result += 'AAAA' * (count // 4)
        # 남은 2칸은 BB
        result += 'BB' * ((count % 4) // 2)

    else:  # '.'
        result += '.'
        i += 1

print(result)
