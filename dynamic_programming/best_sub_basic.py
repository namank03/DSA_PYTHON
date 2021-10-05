def bestSum(target, num_arr):
    if target < 0:
        return None

    if target == 0:
        return []

    # ! here the for loop is trying out all the possible combinations. So, it's good idea to take the shortestCombination variable outside the for loop to track the shortestCombination

    shortestCombination = None

    for i in num_arr:
        remainder = target - i
        remainderResult = bestSum(remainder, num_arr)
        if remainderResult is not None:
            # ! We'll get inside this condition only when there is a path. Now, we need to see which path is the best
            # The below line will generate the path
            remainderResult.append(i)
            combination = remainderResult

            # Logic to evaluate the shortestCombination possible. Notice we not returning early here. Even if we found the path. We're re-running the for-loop to evaluate all possible path and finally we're selecting the shortestCombination out of all
            if shortestCombination is None or len(shortestCombination) > len(
                combination
            ):
                shortestCombination = combination

    return shortestCombination


result = bestSum(7, [2, 4, 1, 3])
print(result)
