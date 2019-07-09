"""
Bubble sort algorithm has all in its name. 
Like Bubble comes out of water towards top. Same way higher values in the array will go towards right.

In Bubble sort the thumb rule is check any 2 values in array and sort them in increasing order.
Now we need to do it for all elements . If length of array is "n" then for n times
Now we need to do this for all the elements "n"
So Time complexity becomes n*n i.e O(nˆ2)

(n-1) comaprision * (n-1) times

spcae complexity; O(1) as no space required for extra array or temp array
 
"""


def sortArrayByBubbleSort(arr):
    for j in range(len(arr)):  # do it for n (len of arr) times 
        for i in range(len(arr) - 1):  # do it for every element
            if arr[i] > arr[i + 1]:  # if current element is greater than next element then swap them
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


arr_1 = [222, 44, 35, 2, 1, 4, 344, 4, 5, 6, 7]
output = sortArrayByBubbleSort(arr_1)
# [1, 2, 4, 4, 5, 6, 7, 35, 44, 222, 344]
