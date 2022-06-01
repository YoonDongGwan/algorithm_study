n = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
min_value, max_value = 1e9, -1e9

def dfs(i, value):
    global min_value, max_value, add, sub, mul, div
    if i == n:
        min_value = min(min_value, value)
        max_value = max(max_value, value)

    if add > 0:
        add -= 1
        dfs(i+1, value + A[i])
        add += 1
    if sub > 0:
        sub -= 1
        dfs(i+1, value - A[i])
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(i+1, value * A[i])
        mul += 1
    if div > 0:
        div -= 1
        dfs(i+1, value // A[i])
        div += 1

dfs(1,A[0])
print(max_value)
print(min_value)
