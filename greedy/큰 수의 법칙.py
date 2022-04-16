n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
result = 0
count = 0
numbers.sort(reverse=True)
for _ in range(m):
    if count < k:
        result += numbers[0]
        count += 1
    else:
        result += numbers[1]
        count = 0
print(result)





