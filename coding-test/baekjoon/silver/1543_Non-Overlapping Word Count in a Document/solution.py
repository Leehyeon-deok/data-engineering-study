doc = input()
word = input()

i = 0
count = 0
word_len = len(word)

while i <= len(doc) - word_len:
    if doc[i:i + word_len] == word:
        count += 1
        i += word_len   # 겹치지 않게 건너뜀
    else:
        i += 1

print(count)
