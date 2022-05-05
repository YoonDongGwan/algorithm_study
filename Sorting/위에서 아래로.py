n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

for i in range(n):
    max_num = i
    for j in range(i + 1, n):
        if array[max_num] < array[j]:
            max_num = j
    array[i], array[max_num] = array[max_num], array[i]
# array = sorted(array, reverse = True) 한 줄로 대체 가능
for i in array:
    print(i, end=' ')

