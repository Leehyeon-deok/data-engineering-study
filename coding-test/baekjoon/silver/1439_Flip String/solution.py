s = input().strip()

count0 = 0
count1 = 0

# 첫 문자로 시작 덩어리 처리
if s[0] == '0':
    count0 += 1
else:
    count1 += 1

# 이전 문자와 다를 때만 덩어리 증가
for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        if s[i] == '0':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))
