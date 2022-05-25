n = list(input())
l = len(n)
m = l // 2
sum_left = 0
sum_right = 0
for i in range(m):
    sum_left += int(n[i])
for i in range(m, l):
    sum_right += int(n[i])

print("LUCKY" if sum_left == sum_right else "READY")