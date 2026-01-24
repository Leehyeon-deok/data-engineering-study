def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def days_until(year, month, day):
    days = 0

    for y in range(1, year):
        days += 366 if is_leap(y) else 365

    month_days = [31, 28, 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31]

    if is_leap(year):
        month_days[1] = 29

    for m in range(1, month):
        days += month_days[m - 1]

    days += day
    return days


# 입력
y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

# gg 판정
if (y2, m2, d2) >= (y1 + 1000, m1, d1):
    print("gg")
else:
    today_days = days_until(y1, m1, d1)
    dday_days = days_until(y2, m2, d2)
    print(f"D-{dday_days - today_days}")
