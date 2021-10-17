def count_of_ele(arr, target):
    start, end = 0, len(arr) - 1

    first_occurrence = last_occurrence = -1

    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            first_occurrence = mid
            end = mid - 1

        elif target < arr[mid]:
            end = mid - 1

        elif target > arr[mid]:
            start = mid + 1

    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            last_occurrence = mid
            start = mid + 1

        elif target < arr[mid]:
            end = mid - 1

        elif target > arr[mid]:
            start = mid + 1

    return last_occurrence - first_occurrence + 1
