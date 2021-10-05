def howsum(target, num_arr, memo={}):
    if target in memo:
        return memo[target]

    if target < 0:
        return None

    if target == 0:
        return []

    for i in num_arr:
        # as we have specified in the basecase the return value is either true or false. Meaning if any one of the recursive call hit the base case True then we can stop the recursion and return early.
        remainder = target - i
        remainderResult = howsum(remainder, num_arr, memo)
        if remainderResult is not None:
            remainderResult.append(i)
            memo[target] = remainderResult
            return memo[target]
    memo[target] = None
    return memo[target]


result = howsum(300, [7, 14])
print(result)
