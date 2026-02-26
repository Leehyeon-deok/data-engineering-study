import sys
input = sys.stdin.read

data = input().split()
t = int(data[0])
idx = 1

for _ in range(t):
    n = int(data[idx])
    m = int(data[idx+1])
    idx += 2
    
    sejun = list(map(int, data[idx:idx+n]))
    idx += n
    sebi = list(map(int, data[idx:idx+m]))
    idx += m
    
    if max(sejun) >= max(sebi):
        print("S")
    else:
        print("B")
