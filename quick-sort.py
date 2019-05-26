"""

Takes last element as pivot, places the pivot element at its correct position in sorted
array, and places all smaller than pivot  to left of pivot and all greater elements to right

"""



def partition(arr, low, high):
    ind = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            ind = ind + 1
            arr[ind], arr[j] = arr[j], arr[ind]
    arr[ind + 1], arr[high] = arr[high], arr[ind + 1]
    return (ind + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)  # Separately sort elements before  partition
        quickSort(arr, pi + 1, high)  # Separately sort elements after  partition


    return arr
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
print(quickSort(arr, 0, n - 1))
