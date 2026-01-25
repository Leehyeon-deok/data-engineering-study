A, B, N = map(int, input().split())

r = A % B  # 초기 나머지

for _ in range(N):
    r *= 10
    digit = r // B
    r %= B

print(digit)
