"""

Theta(nLog(n)).

Auxiliary Space: O(n)


"""


def mergeSort(arr):
    if len(arr) > 1:
        middle_ind = len(arr) // 2  # Finding the mid of the array
        left_arr = arr[:middle_ind]  # Dividing the array elements
        right_arr = arr[middle_ind:]  # into 2 halves

        mergeSort(left_arr)  # Sorting the first half
        mergeSort(right_arr)  # Sorting the second half

        i = 0  # ind for left_arr
        j = 0  # ind for right_arr
        k = 0  # ind for main arr

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                # if element of left_arr is smaller than right_arr element
                # then add this number to arr
                arr[k] = left_arr[i]
                i += 1
            else:
                # if element of right_arr is smaller than left_arr element
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # Checking if any element was left from left_arr
        # if left then add it to the end at is largest of them
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        # Checking if any element was left from right_arr
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    return arr

print(mergeSort([1, 45, 2, 12, 74, 22]))
