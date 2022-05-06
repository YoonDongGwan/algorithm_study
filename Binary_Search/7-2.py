a = [0,2,4,6,8,10,12,14,16,18]

def binary_search(array, target, start, end):
    middle = (start + end) // 2
    if target == array[middle]:
        return middle
    elif target < array[middle]:
        return binary_search(array, target, start, middle-1)
    elif target > array[middle]:
        start = middle
        return binary_search(array, target, middle+1, end)

result = binary_search(a, 18, 0, len(a)-1)

print(result)