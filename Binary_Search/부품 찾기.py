def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if target == arr[mid]:
        return mid
    elif target > arr[mid]:
        return binary_search(arr, target, mid+1, end)
    else:
        return binary_search(arr, target, start, mid-1)


n = int(input())

parts_list = list(map(int, input().split()))

parts_list.sort()

m = int(input())

search_list = list(map(int, input().split()))

result = []
for i in search_list:
    res = binary_search(parts_list, i, 0, len(parts_list) - 1)
    if res ==  None:
        result.append("No")
    else:
        result.append("Yes")

print(result)