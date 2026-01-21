words = input().strip().upper()

count=[0] * 26

for c in words:
    count[ord(c)-ord('A')] += 1

max_count = max(count)

if count.count(max_count) > 1 :
    print("?")
else:
    print(chr(count.index(max_count)+ord('A')))
