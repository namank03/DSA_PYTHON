def merge(arr1, arr2):
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            k = j
            while k < len(arr2) - 1 and arr2[k] > arr2[k + 1]:
                k += 1
            arr2[k], arr2[j] = arr2[j], arr2[k]
        else:
            j += 1


arr1 = [1, 3, 5, 7]
arr2 = [0, 2, 6, 8, 9]


merge(arr1, arr2)
