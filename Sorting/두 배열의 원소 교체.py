n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# 내가 한거
# max_index = min_index = 0
# while k > 0:
#     for i in range(1, n):
#         if a[min_index] > a[i]:
#             min_index = i
#         if b[max_index] < b[i]:
#             max_index = i
#     if a[min_index] >= b[max_index]:
#         break
#     a[min_index], b[max_index] = b[max_index], a[min_index]
#     k -= 1
#
# print(sum(a))
# 모범 답안
a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))