def k_th_max_min(arr, k):
    max = [arr[0]] * k
    min = [arr[0]] * k

    print(max, min)

    for i in arr:
        if i > max[0]:
            max[1:] = max[:-1]
            max[0] = i
        if i < min[0]:
            min[1:] = min[:-1]
            min[0] = i

    return max, min


print(k_th_max_min([1, 3, 4, 10, 90, -1], 3))
