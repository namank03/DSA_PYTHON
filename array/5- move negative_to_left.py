def move_negatives(arr):
    # * HINT: Here we're using two pointers from differnt sides of an arary. If we've the positive element on left side and the negative element on right, then we swap the elements. Otherwise, we make the pointers come closer.

    # ! Another way to solve the problem in O(n) time conplexity is to do Quicksort.

    l = 0
    r = len(arr) - 1

    while l < r:
        if arr[l] < 0 and arr[r] < 0:
            l += 1
        elif arr[l] < 0 and arr[r] > 0:
            l += 1
            r -= 1
        elif arr[l] > 0 and arr[r] < 0:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        else:
            r -= 1

    return arr


print(move_negatives([1, -2, 3, -9, 3, -8, 3]))
