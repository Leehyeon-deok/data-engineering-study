if N == 0:
    print(0)
    exit()

box_count = 1
current_weight = 0

for book in books:
    if current_weight + book <= M:
        current_weight += book
    else:
        box_count += 1
        current_weight = book

print(box_count)
