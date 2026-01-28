group = 1

while True:
    n = int(input())
    if n == 0:
        break

    papers = []
    names = []

    for _ in range(n):
        line = input().split()
        names.append(line[0])
        papers.append(line[1:])

    if group > 1:
        print()

    print(f"Group {group}")

    nasty_found = False

    for i in range(n):              # 종이 주인
        for j in range(n - 1):      # 메시지
            if papers[i][j] == 'N':
                writer = (i - (j + 1) + n) % n
                print(f"{names[writer]} was nasty about {names[i]}")
                nasty_found = True

    if not nasty_found:
        print("Nobody was nasty")

    group += 1
