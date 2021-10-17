

def binarySearchReverseSortedArr(arr, target):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return mid

        elif target < arr[mid]:
            start = mid + 1

        elif target > arr[mid]:
            end = mid - 1

    return -1
