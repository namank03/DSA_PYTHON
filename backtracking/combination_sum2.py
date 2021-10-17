
def backtrack(result_list, tempList, nums, target):
    # Add condition here to validate the state before adding it to the result list
    if target == 0:
        result_list.append(tuple(tempList))

    if target < 0:
        return

    for i in range(len(nums)):
        # add condition here to make sure the current candidate is a valid candidate
        tempList.append(nums[i])
        # explore via dfs
        # ! Notice the change in the line below
        backtrack(result_list, tempList, nums[i + 1:], target - nums[i])
        # remove the candidate
        tempList.pop()


def combination_sum(nums, target):
    result_list = []
    nums = sorted(nums)
    backtrack(result_list, [], nums, target)
    return set(result_list)


print(combination_sum([6, 1, 2, 5], 8))
# vs.make_animation("images/comb_sum.gif", delay=2)
