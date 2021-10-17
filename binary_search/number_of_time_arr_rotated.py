
def no_of_time_arr_rotated(arr):
    # This program is not completed and may fail several test-cases.
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2

        if arr[end] >= arr[mid]:
            end = mid - 1

        elif arr[start] <= arr[mid]:
            start = mid + 1

    return mid


print(no_of_time_arr_rotated([11, 12, 15, 18, 2, 5, 6, 8]))
