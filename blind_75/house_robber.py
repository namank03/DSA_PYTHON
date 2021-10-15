def house_robber(arr, memo={}):
    if len(arr) == 1:
        return arr[0]

    if len(arr) < 1:
        return 0

    arr_str = "".join(map(str, arr))
    if arr_str in memo:
        return memo[arr_str]

    memo[arr_str] = max(arr[-1] + house_robber(arr[:-2], memo),
                        house_robber(arr[:-1], memo))
    return memo[arr_str]


print(house_robber([1, 2, 0, 3, 1]))
