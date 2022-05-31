from collections import deque

n, k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

m = len(graph[0])
s, a, b = map(int, input().split())

h = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            h.append([graph[i][j],0,i,j])
h.sort()
q = deque(h)

print(q)

while q:
    v = q.popleft()
    t, x, y = v[1], v[2], v[3]
    if t == s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = v[0]
                q.append([v[0], t+1, nx, ny])

print(graph)
print(graph[a-1][b-1])


