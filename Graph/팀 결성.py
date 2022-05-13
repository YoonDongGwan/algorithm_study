def find_friendly(team, x):
    if team[x] != x:
        team[x] = find_friendly(team, team[x])
    return team[x]


def union_friendly(team, x, y):
    a = find_friendly(team, x)
    b = find_friendly(team, y)
    if a < b:
        team[b] = a
    else:
        team[a] = b

n ,m = map(int, input().split())

team = [0] * (n + 1)

for i in range(1, n+1):
    team[i] = i
for _ in range(m):
    o, a, b = map(int, input().split())
    if o == 0:
        union_friendly(team, a, b)
    else:
        if find_friendly(team, a) == find_friendly(team, b):
            print("Yes")
        else:
            print("No")

