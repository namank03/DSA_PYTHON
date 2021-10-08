def knapSack(wt, val, W, n, memo={}):
    if (W, n) in memo.keys():
        return memo[(W, n)]

    if n == 0 or W == 0:
        return 0

    if W - wt[n-1] >= 0:
        memo[(W, n)] = max(val[n-1] + knapSack(wt, val,
                                               W - wt[n-1], n-1, memo), knapSack(wt, val, W, n-1, memo))
    else:
        memo[(W, n)] = knapSack(wt, val, W, n - 1, memo)

    return memo[(W, n)]


values = [1, 2, 3]
weight = [4, 5, 6]

W = 3

print(knapSack(weight, values, W, 3))
