n = int(input())
a = list(map(int, input().split()))

d = [0] * n
d[0] ,d[1] = a[0], max(a[0],a[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+a[i])

print(d[n-1])