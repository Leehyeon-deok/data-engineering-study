n = int(input())

count = 0
num = 665  # 666부터 검사하기 위해 665에서 시작

while True:
    num += 1
    if "666" in str(num):
        count += 1
        if count == n:
            print(num)
            break
