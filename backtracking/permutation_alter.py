def backtrack(result_list, tempList, nums):
    # Add condition here to validate the state before adding it to the result list
    result_list.append(tempList[:])
    for i in range(len(nums)):
        # add condition here to make sure the current candidate is a valid candidate
        # Here we're passing the same array without dec the size but there's a catch we're also not backtracking if the element is already in the tempList
        if nums[i] in tempList:
            continue
        tempList.append(nums[i])
        # explore via dfs
        backtrack(result_list, tempList, nums)
        # remove the candidate
        tempList.pop()


def permutation_alter(nums):
    result_list = []
    nums = sorted(nums)
    backtrack(result_list, [], nums)
    return result_list


print(permutation_alter([1, 2, 3]))
