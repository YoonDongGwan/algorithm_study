n, m = map(int, input().split())
coin = [0] * n
d = [10001] * (m+1)
for i in range(n):
    coin[i] = int(input())
d[0] = 0

for i in range(m+1):
    for j in coin:
        if i - j >= 0:
            if d[i-j] != 10001:
                d[i] = min(d[i-j]+1, d[i])
print(d[m]) if d[m] != 10001 else print(-1)