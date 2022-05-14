s = list(map(int,input()))
s.sort(reverse=True)
result = s[0]
for i in range(1, len(s)):
    if s[i] == 0:
        continue
    elif s[i] == 1:
        result += 1
    else:
        result *= s[i]

print(result)