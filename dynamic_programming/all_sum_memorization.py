import copy


def allSum(target, num_arr, memo={}):
    if target in memo:
        return copy.deepcopy(memo[target])

    if target < 0:
        return None

    if target == 0:
        # If we wanna construct all possible paths, then we need to start with nested list and each valid part will then be returnred and added to this nested list
        return [[]]

    # Variable to store the result
    allCombinations = None
    for i in num_arr:
        remainder = target - i
        # This time instead of the result it'll gonna return the list of the result. What we specified in the base case return value. That's what we get returned to us
        remainderResultList = allSum(remainder, num_arr, memo)
        if remainderResultList is not None:
            # This condition will make sure that we hit the correct base case and we've found the result list.
            for remainderResult in remainderResultList:
                #! TIP: IMP STEP Construct the remainedResult for each valid remainder array
                remainderResult.append(i)
            if allCombinations is None:
                allCombinations = remainderResultList
            else:
                # ! here we add all the result to the allsum array
                allCombinations += remainderResultList

    memo[target] = copy.deepcopy(allCombinations)
    return allCombinations


result = allSum(7, [3, 1, 4])
print(result)
