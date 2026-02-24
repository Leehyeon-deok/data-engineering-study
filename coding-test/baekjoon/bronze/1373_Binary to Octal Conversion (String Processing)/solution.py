import sys

s = sys.stdin.readline().strip()
result = []

# 앞쪽 남은 부분 먼저 처리
first = len(s) % 3
if first != 0:
    result.append(str(int(s[:first], 2)))

# 나머지
for i in range(first, len(s), 3):
    result.append(str(int(s[i:i+3], 2)))

print(''.join(result))
