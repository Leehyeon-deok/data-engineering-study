A, B = map(int, input().split())

sequence = []
num = 1

# B번째까지 수열 만들기
while len(sequence) < B:
    sequence.extend([num] * num)
    num += 1

# A~B 구간 합
print(sum(sequence[A-1:B]))
