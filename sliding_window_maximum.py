def printMax(arr, k):
    n = len(arr)

    for i in range(n - k + 1):
        max = arr[i]

        for j in range(1, k):
            max = arr[i + j]

            if arr[i + j] > max:
                max = arr[i + j]

        print(str(max) + " ", end = "")


if __name__ == "__main__":
    arr = [2, 1, 2, -1, 3]
    k = 2
    printMax(arr, k)
