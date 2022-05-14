n = int(input())
fear = list(map(int, input().split()))
i = 0
count = 0
fear.sort(reverse=True)

while i < len(fear):
    m = fear[i]
    i += m
    count += 1

print(count)