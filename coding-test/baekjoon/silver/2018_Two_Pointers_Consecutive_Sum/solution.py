N = int(input())
count = 0

i = 1
while i * i <= N:
    if N % i == 0:
        if i % 2 == 1:
            count += 1
        if (N // i) != i and (N // i) % 2 == 1:
            count += 1
    i += 1

print(count)
