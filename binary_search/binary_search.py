def binarySearch(arr, target):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            end = mid - 1

        elif arr[mid] < target:
            start = mid + 1

    return -1
