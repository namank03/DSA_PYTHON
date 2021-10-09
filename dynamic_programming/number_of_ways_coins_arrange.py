def min_coins(target_sum, arr, memo={}):
    if target_sum < 0:
        return 0

    if target_sum == 0:
        return 1

    if target_sum in memo:
        return memo[target_sum]

    memo[target_sum] = sum(min_coins(target_sum - i, arr, memo)
                           for i in arr)

    return memo[target_sum]


print(min_coins(5, [2, 3]))
