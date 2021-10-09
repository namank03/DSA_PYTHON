import copy


def bestSum(target, num_arr, memo={}):
    if target in memo:
        return memo[target]

    if target < 0:
        return -1

    if target == 0:
        return 0

    shortestCombination = -1

    for i in num_arr:
        remainder = target - i
        remainderResult = bestSum(remainder, num_arr, memo)
        if remainderResult != -1:
            remainderResult += 1

            if shortestCombination == -1 or shortestCombination > remainderResult:
                shortestCombination = remainderResult

    memo[target] = shortestCombination
    return memo[target]


result = bestSum(5, [2, 1, 3, 5])
print(result)
