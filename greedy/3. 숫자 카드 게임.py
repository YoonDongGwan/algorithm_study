n, m = map(int, input().split())
result = 0
for _ in range(n):
    array = list(map(int, input().split()))
    minimum_value = min(array)
    if result == 0 or result < minimum_value:
        result = minimum_value

print(result)