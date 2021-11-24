
# def no_of_time_arr_rotated(arr):
#     start, end = 0, len(arr) - 1
#     while start <= end:
#         mid = (start + end) // 2

#         if arr[mid] >= arr[end]:
#             end = mid - 1

#         elif arr[mid] >= arr[start]:
#             start = mid + 1

#     return mid


def countRotations(arr):
    n = len(arr)
    start = 0
    end = n-1
    # finding the index of minimum of the array
    # index of min would be equal to number to rotation
    while start <= end:

        mid = start+(end-start)//2
        # Calculating the previous(prev) and next(nex) index of mid

        # prev = (mid-1+n) % n
        # nex = (mid+1) % n

        # # Checking if mid is minimum
        # if arr[mid] < arr[prev] and arr[mid] <= arr[nex]:
        #     return mid

        # if not selecting the unsorted part of array
        if arr[mid] < arr[start]:
            end = mid-1
        elif arr[mid] > arr[end]:
            start = mid+1

    return mid


print(countRotations([11, 12, 15, 18, 2, 5, 6, 8]))
