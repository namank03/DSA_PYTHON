def max_min(arr):
    max = arr[0]
    min = arr[0]
    for i in arr:
        if i > max:
            max = i
        if i < min:
            min = i

    return max, min


print(max_min([1, 3, 4, 10, 90, -1]))
