n = int(input())
students = [list(map(int, input().split())) for _ in range(n)]

max_count = -1
leader = 0

for i in range(n):
    count = 0
    for j in range(n):
        if i == j:
            continue
        
        # 1~5학년 비교
        for k in range(5):
            if students[i][k] == students[j][k]:
                count += 1
                break  # 한 번만 같은 반이면 OK

    # 최대값 갱신 (번호 작은 학생 우선)
    if count > max_count:
        max_count = count
        leader = i

print(leader + 1)
