x = input().strip()
count = 0

while len(x) > 1:
    s = 0
    for c in x:
        s += int(c)
    x = str(s)
    count += 1

print(count)
if x in ('3', '6', '9'):
    print("YES")
else:
    print("NO")
