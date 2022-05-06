n, m = map(int, input().split())

length_list = list(map(int, input().split()))

def binary_search(arr, target, start, end):
    if start > end:
        return
    mid = (start+end) // 2
    sum = 0
    for length in arr:
        sum += length - mid if length - mid > 0 else 0

    if sum > target:
        return binary_search(arr, target, mid+1, end)
    elif sum == target:
        return mid
    else:
        return binary_search(arr, target, start, end-1)

print(binary_search(length_list, m, 0, max(length_list)))