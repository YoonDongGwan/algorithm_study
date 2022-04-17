location = input()
column = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
row = [1, 2, 3, 4, 5, 6, 7, 8]
two = [2, -2]
one = [1, -1]
result = 0
temp = location[0]
for i in range(2):
    c = chr(ord(temp) + two[i])
    if c in column:
        for j in range(2):
            r = int(location[1]) + one[j]
            if r in row:
                result += 1
for i in range(2):
    r = int(location[1]) + two[i]
    if r in row:
        for j in range(2):
            c = chr(ord(location[0]) + one[j])
            if c in column:
                result += 1
print(result)


