n = int(input())
origin = n
count = 0

while True :
    a = n//10
    b = n%10
    n = b*10 + (a+b)%10

    count +=1

    if n == origin:
        break


print(count)
