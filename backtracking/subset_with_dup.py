def backtrack(result_list, tempList, nums):

    # Add condition here to validate the state before adding it to the result list
    result_list.add(tuple(tempList[:]))
    for i in range(len(nums)):
        # add condition here to make sure the current candidate is a valid candidate
        if i > 1 and nums[i] == nums[i-1]:
            continue
        tempList.append(nums[i])
        # explore via dfs
        backtrack(result_list, tempList, nums[i+1:])
        # remove the candidate
        tempList.pop()


def main_func(nums):
    result_list = set()
    nums = sorted(nums)
    backtrack(result_list, [], nums)
    return result_list


print(main_func([1, 2, 2]))
