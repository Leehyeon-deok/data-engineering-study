X = int(input())

line = 1
count = 0

# 몇 번째 대각선인지 찾기
while count + line < X:
    count += line
    line += 1

# 대각선 내 위치
idx = X - count

# 대각선 번호가 홀수일 때
if line % 2 == 1:
    numerator = line - idx + 1
    denominator = idx
else:
    numerator = idx
    denominator = line - idx + 1

print(f"{numerator}/{denominator}")
