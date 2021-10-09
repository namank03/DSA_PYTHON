def best_sum_length(arr, target, n):

    if n == 0:
        return 0

    if target == 0:
        return 1

    if target >= arr[n-1]:
        return min(
            1 + best_sum_length(arr, target - arr[n-1], n - 1),
            best_sum_length(arr, target, n - 1)
        )
    else:
        return best_sum_length(arr, target, n - 1)


print(best_sum_length([3, 1], 7, 2))
