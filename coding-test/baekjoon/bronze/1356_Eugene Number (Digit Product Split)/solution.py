N = input()

is_eugene = False

for i in range(1, len(N)):
    left = N[:i]
    right = N[i:]

    left_mul = 1
    right_mul = 1

    for x in left:
        left_mul *= int(x)

    for x in right:
        right_mul *= int(x)

    if left_mul == right_mul:
        is_eugene = True
        break

print("YES" if is_eugene else "NO")
