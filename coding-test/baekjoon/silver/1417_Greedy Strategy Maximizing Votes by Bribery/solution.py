import sys
input = sys.stdin.readline

N = int(input())

me = int(input())  # 다솜이 득표수
others = []

for _ in range(N - 1):
    others.append(int(input()))

count = 0

while others:
    max_vote = max(others)
    
    if me > max_vote:
        break
    
    idx = others.index(max_vote)
    others[idx] -= 1
    me += 1
    count += 1

print(count)
