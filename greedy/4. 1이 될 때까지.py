n, k = map(int, input().split())
result = 0

while n > 1:
    if n < k:
        result += n - 1
        break
    else:
        remainder = n % k
        n -= remainder
        n //= k
        result += remainder + 1

print(result)


