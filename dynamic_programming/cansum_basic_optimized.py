def cansum(target, num_arr):
    if target < 0:
        return False

    if target == 0:
        return True

    for i in num_arr:
        # as we have specified in the basecase the return value is either true or false. Meaning if any one of the recursive call hit the base case True then we can stop the recursion and return early.
        remainder = target - i
        if cansum(remainder, num_arr):
            return True

    return False


result = cansum(7, [3, 2])
print(result)
