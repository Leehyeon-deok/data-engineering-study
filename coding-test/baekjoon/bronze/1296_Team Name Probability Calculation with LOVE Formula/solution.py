import sys

yeondu = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())

teams = [sys.stdin.readline().strip() for _ in range(n)]

def get_probability(name):
    total = yeondu + name
    
    L = total.count('L')
    O = total.count('O')
    V = total.count('V')
    E = total.count('E')
    
    return ((L+O) * (L+V) * (L+E) *
            (O+V) * (O+E) * (V+E)) % 100

max_score = -1
answer = ""

for team in sorted(teams):  # 사전순 정렬
    score = get_probability(team)
    
    if score > max_score:
        max_score = score
        answer = team

print(answer)
