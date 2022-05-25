n = list(input())
n.sort()
sum_number = 0
result = ''
for i in range(len(n)):
    if '0'<= n[i] <= '9':
        sum_number += int(n[i])
    else:
        result += n[i]

print(result+str(sum_number))