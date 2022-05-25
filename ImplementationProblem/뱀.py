n = int(input())
k = int(input())
apple = []
for i in range(k):
    apple.append(list(map(int, input().split())))

l = int(input())
t = []
dir = []
for i in range(l):
    x, c = input().split()
    t.append(int(x))
    dir.append(c)

d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
body = [[1, 1]]

a = [3, 4]

i, j, result = 0, 0, 0
dir_len = len(dir)
meet_body = False

while 0 < body[0][0] < n+1 and 0 < body[0][1] < n+1 and (not meet_body):
    if j < dir_len:
        if result == t[j]:
            if dir[j] == 'D':
                i += 1
            else:
                i -= 1
            j += 1
    body.insert(1, [body[0][0], body[0][1]])

    body[0][0] += d[i][0]
    body[0][1] += d[i][1]

    if body.count([body[0][0], body[0][1]]) > 1:
        meet_body = True

    if [body[0][0], body[0][1]] in apple:
        apple.remove([body[0][0], body[0][1]])
    else:
        body.pop(-1)


    print(str(result)+"~"+str(result+1))
    print(body)
    result += 1

print(result)