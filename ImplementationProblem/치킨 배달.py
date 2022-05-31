from itertools import combinations

n, m = map(int, input().split())
city = []
chicken = []
house = []
result = int(1e9)
for _ in range(n):
    city.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append([i,j])
        elif city[i][j] == 1:
            house.append([i,j])

combi = list(combinations(chicken, m))

print(combi)

for c in combi:
    sum = 0
    for h in house:
        chicken_distance = int(1e9)
        for i in range(m):
            chicken_distance = min(chicken_distance, abs(h[0]-c[i][0]) + abs(h[1]-c[i][1]))
        sum += chicken_distance
    result = min(result, sum)



print(result)