n = int(input())
count = 0

for _ in range(n):
    word = input()
    seen = set()
    is_group = True

    for i in range(len(word)):
        if word[i] not in seen:
            seen.add(word[i])
        else:
            if word[i] != word[i - 1]:
                is_group = False
                break

    if is_group:
        count += 1

print(count)
