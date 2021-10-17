def backtrack(result_list, tempList, nums):
    # Add condition here to validate the state before adding it to the result list
    op = tempList[:]
    if not nums and op not in result_list:
        result_list.append(tempList[:])
    for i in range(len(nums)):
        # add condition here to make sure the current candidate is a valid candidate

        tempList.append(nums[i])
        # explore via dfs
        backtrack(result_list, tempList, nums[:i] + nums[i+1:])
        # remove the candidate
        tempList.pop()


def permutations(nums):
    result_list = []
    nums = sorted(nums)
    backtrack(result_list, [], nums)
    return result_list


print(permutations([1, 1, 2]))
