n = int(input())
plan = list(input().split())
x = y = 1
for c in plan:
   if c == 'L' and y > 1:
       y -= 1
   elif c == 'R' and y < n:
       y += 1
   elif c == 'U' and x > 1:
       x -= 1
   elif c == 'D' and x < n:
       x += 1

print(x, y)
