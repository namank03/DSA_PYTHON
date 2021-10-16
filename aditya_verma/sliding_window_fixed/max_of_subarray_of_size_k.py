import math


def max_subarray_k(arr, k):
    i = j = 0
    g_r = []
    c_r = []

    c_m = -math.inf

    while j < len(arr):

        # initial calculation
        if arr[j] > c_m:
            c_m = arr[j]

        # moving window
        if j-i+1 < k:
            j += 1

        elif j-i+1 == k:
            # Calculations
            c_r.insert(0, c_m)
            g_r.append(c_r[0])

            # sliding window
            if arr[i] == c_r[0]:
                c_r.pop()

            j += 1
            i += 1

    return g_r


print(max_subarray_k([2, 3, 1, 4, 9, 0, 1], 3))
