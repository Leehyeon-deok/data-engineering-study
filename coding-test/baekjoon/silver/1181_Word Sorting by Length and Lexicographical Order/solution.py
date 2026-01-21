N = int(input())

words = set()  # 중복 제거
for _ in range(N):
    words.add(input().strip())

# 정렬: (길이, 사전순)
words = sorted(words, key=lambda x: (len(x), x))

for word in words:
    print(word)
