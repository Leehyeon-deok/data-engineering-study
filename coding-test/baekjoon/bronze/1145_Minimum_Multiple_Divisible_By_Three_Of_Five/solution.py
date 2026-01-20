nums = list(map(int,input().split()))

x = 1

while True:
    cnt = 0

    for n in nums :
        if x % n == 0:
            cnt += 1

    if cnt >= 3:
        print(x)
        break

    x += 1
        
