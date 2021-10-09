#! Optimization via returning early.
def cansum(target, num_arr, memo={}):
    if target < 0:
        return False

    if target == 0:
        return True

    if target in memo:
        return memo[target]

    for i in num_arr:
        # as we have specified in the basecase the return value is either true or false. Meaning if any one of the recursive call hit the base case True then we can stop the recursion and return early.
        remainder = target - i
        if cansum(remainder, num_arr):
            # ! remember this the trick to memorization is to save the value in memo before returning it
            memo[target] = True
            return True
    # ! remember this the trick to memorization is to save the value in memo before returning it
    memo[target] = False
    return False


result = cansum(701, [9, 11])
print(result)
