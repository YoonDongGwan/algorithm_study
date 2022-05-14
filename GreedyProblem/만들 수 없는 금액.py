n = int(input())
coins = sorted(list(map(int, input().split())))
i = 1

for x in coins:
    if i < x:
        break
    i += x

print(i)


