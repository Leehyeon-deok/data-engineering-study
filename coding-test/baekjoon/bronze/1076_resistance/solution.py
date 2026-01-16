# 색깔별 값과 곱을 딕셔너리로 정의
resistor = {
    "black": (0, 1),
    "brown": (1, 10),
    "red": (2, 100),
    "orange": (3, 1000),
    "yellow": (4, 10000),
    "green": (5, 100000),
    "blue": (6, 1000000),
    "violet": (7, 10000000),
    "grey": (8, 100000000),
    "white": (9, 1000000000)
}

# 입력
c1 = input().strip()
c2 = input().strip()
c3 = input().strip()

# 계산
value = (resistor[c1][0] * 10 + resistor[c2][0]) * resistor[c3][1]

# 출력
print(value)
