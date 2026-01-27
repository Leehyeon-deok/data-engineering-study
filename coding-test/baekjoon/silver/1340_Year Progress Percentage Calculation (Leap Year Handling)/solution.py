import sys

def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0

month_days = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

line = sys.stdin.readline().strip()

month, rest = line.split(" ", 1)
day_part, time_part = rest.split(" ", 1)

day = int(day_part.replace(",", ""))
year, clock = time_part.split(" ")
hour, minute = map(int, clock.split(":"))
year = int(year)

days_in_year = 366 if is_leap(year) else 365
total_minutes = days_in_year * 24 * 60

passed_days = 0
for m in month_days:
    if m == month:
        break
    passed_days += month_days[m]

if is_leap(year) and month not in ["January", "February"]:
    passed_days += 1

passed_days += (day - 1)

passed_minutes = passed_days * 1440 + hour * 60 + minute

percentage = (passed_minutes / total_minutes) * 100
print(percentage)
