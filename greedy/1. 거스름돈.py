coin_list = [500, 100, 50, 10]

n = int(input())
result = 0
for coin in coin_list:
    if n >= coin and n > 0:
        count = n // coin
        n -= count * coin
        result += count
print(result)