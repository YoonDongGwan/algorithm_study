# 답지

from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

queue = deque([x])

while queue:
    now = queue.popleft()

    for i in graph[now]:
        if distance[i] == -1:
            queue.append(i)
            distance[i] = distance[now] + 1

check = False
for i in range(len(distance)):
    if distance[i] == k:
        print(i)
        check = True

if not check:
    print(-1)