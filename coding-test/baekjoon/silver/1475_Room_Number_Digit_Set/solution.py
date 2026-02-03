N = input().strip()

count = [0] * 10

# 각 숫자 개수 세기
for ch in N:
    count[int(ch)] += 1

# 6과 9는 묶어서 계산
six_nine = count[6] + count[9]
count[6] = (six_nine + 1) // 2
count[9] = 0

# 가장 많이 필요한 숫자가 세트 수
print(max(count))
