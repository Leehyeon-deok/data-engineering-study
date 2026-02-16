import math

N = int(input())
answer = float('inf')

limit = int(math.sqrt(N)) + 2

for x in range(2, limit):
    y = (N + x - 1) // x
    if y < 2:
        y = 2
    perimeter = 2 * (x + y - 2)
    answer = min(answer, perimeter)

print(answer)
