def turn_right(arr):
    l = len(arr)
    new_arr = [[] for _ in range(l)]
    for i in range(l):
        for j in range(l-1, -1, -1):
            new_arr[i].append(arr[j][i])
    return new_arr

def check(arr):
    x = len(arr) // 3
    for i in range(x, x * 2):
        for j in range(x, x * 2):
            if arr[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    checkbox = [[0] * (n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            checkbox[i+n][j+n] = lock[i][j]

    for i in range(4):
        key = turn_right(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        checkbox[x+i][y+j] += key[i][j]

                if check(checkbox) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        checkbox[x + i][y + j] -= key[i][j]

    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(str(solution(key,lock)))
