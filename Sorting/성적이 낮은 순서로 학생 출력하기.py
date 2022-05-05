n = int(input())
array = []
for _ in range(n):
    name, score = input().split()
    array.append((name, int(score)))

def setting(data):
    return data[1]

result = sorted(array, key=setting)

for i in range(n):
    print(result[i][0], end=' ')