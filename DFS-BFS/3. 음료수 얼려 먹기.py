n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))
result = 0

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m: # x y가 그래프 이상 혹은 이하의 인덱스를 방문할 때
        return False
    if graph[x][y] == 0: # 방문하지 않은 곳이면
        graph[x][y] = 1 # 방문 표시를 하고
        dfs(x - 1, y)   # 상
        dfs(x + 1, y)   # 하
        dfs(x, y - 1)   # 좌
        dfs(x, y + 1)   # 우로 다시 탐색
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)