import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    
    if A == 0 and B != 0:
        print("no")
    else:
        print("yes")
