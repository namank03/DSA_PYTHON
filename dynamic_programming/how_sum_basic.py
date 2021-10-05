def howsum(target, num_arr):
    if target < 0:
        return None

    if target == 0:
        #! whenever we want to evaluate the path or the values used to obtain the final result, we 1st start with the empty list and then add the values to this empty list when the solution is found.
        return []

    for i in num_arr:
        # as we have specified in the basecase the return value is either true or false. Meaning if any one of the recursive call hit the base case True then we can stop the recursion and return early.
        remainder = target - i
        remainderResult = howsum(remainder, num_arr)
        if remainderResult is not None:
            #! if remainderResult is non None that means we've evaluated the soultion and now we can add the result
            remainderResult.append(i)
            return remainderResult

    return None


result = howsum(7, [3, 2])
print(result)
