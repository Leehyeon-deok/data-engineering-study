w,x,y,h = map(int(),input().split())

result= min(x,h-y,w-x,y)

print(result)
