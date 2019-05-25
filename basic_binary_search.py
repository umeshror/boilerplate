def binarySearch(arr, value_to_find):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) / 2
        if arr[mid] == value_to_find:
            return mid
        elif arr[mid] < value_to_find:
            low = mid + 1
        else:
            high = mid - 1
    return -1



x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

output = binarySearch(x, 2)
# output should be 1
print(output == 1)
