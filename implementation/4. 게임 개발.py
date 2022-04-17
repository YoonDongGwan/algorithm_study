n, m = map(int, input().split())
a, b, d = map(int, input().split())
world = []
for _ in range(n):
    world.append(list(map(int, input().split())))

direction = ['N', 'E', 'S', 'W']
visited = []
now_location = (a, b)
visited.append(now_location)
stuck_count = 0
while True:
    d -= 1
    if d < 0:
        d = 3
    now_d = direction[d]
    from_location = now_location
    if now_d == 'N' and now_location[0] > 0:
        now_location = (now_location[0] - 1, now_location[1])
    elif now_d == 'E' and now_location[1] < m:
        now_location = (now_location[0], now_location[1] + 1)
    elif now_d == 'S' and now_location[0] < n:
        now_location = (now_location[0] + 1, now_location[1])
    elif now_d == 'W' and now_location[1] > 0:
        now_location = (now_location[0], now_location[1] - 1)

    if (now_location not in visited) and (world[now_location[0]][now_location[1]] == 0):
        visited.append(now_location)
        stuck_count = 0
    else:
        now_location = from_location
        stuck_count += 1
    if stuck_count == 4:
        break

print(len(visited))