def first_occurrence(arr, target):
    start, end = 0, len(arr) - 1

    res = -1
    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            res = mid
            end = mid - 1

        elif target < arr[mid]:
            end = mid - 1

        elif target > arr[mid]:
            start = mid + 1

    return res


print(first_occurrence([2, 4, 10, 10, 10, 18, 20], 10))


def last_occurrence(arr, target):
    start, end = 0, len(arr) - 1

    res = -1
    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            res = mid
            start = mid + 1

        elif target < arr[mid]:
            end = mid - 1

        elif target > arr[mid]:
            start = mid + 1

    return res


print(last_occurrence([2, 4, 10, 10, 10, 18, 20], 10))
