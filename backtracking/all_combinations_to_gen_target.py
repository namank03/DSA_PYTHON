def backtrack(result_list, tempList, n, target):
    if target == 0:
        result_list.add(tuple(sorted(tempList[:])))
    if target < 0:
        return
    for i in n:
        tempList.append(i)
        backtrack(result_list, tempList, n, target - i)
        tempList.pop()


def combinations(n, target):
    result = set()
    backtrack(result, [], n, target)
    return result
