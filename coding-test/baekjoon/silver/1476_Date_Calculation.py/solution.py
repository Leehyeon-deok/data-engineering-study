E, S, M = map(int, input().split())

year = 1

while True:
    e = year % 15
    s = year % 28
    m = year % 19

    if e == 0:
        e = 15
    if s == 0:
        s = 28
    if m == 0:
        m = 19

    if e == E and s == S and m == M:
        print(year)
        break

    year += 1
