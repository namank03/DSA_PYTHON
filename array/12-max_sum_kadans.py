def max_sum(arr):
    if len(arr) == 0:
        return 0
    c_m = g_m = arr[0]
    for i in arr[1:]:
        c_m = max(i, c_m + i)
        if c_m > g_m:
            g_m = c_m

    return g_m


print(max_sum([-1, -2, -3, 9, 5]))
