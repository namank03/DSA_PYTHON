
from visualiser.visualiser import Visualiser as vs


@vs(node_properties_kwargs={"shape": "record", "color": "#f57542", "style": "filled", "fillcolor": "grey"})
def backtrack(result_list, tempList, nums, used):
    # Add condition here to validate the state before adding it to the result list
    if len(tempList) == len(nums):
        result_list.append(tempList[:])
    for i in range(len(nums)):
        # add condition here to make sure the current candidate is a valid candidate
        if(used[i] or i > 0 and nums[i] == nums[i-1] and not used[i - 1]):
            continue
        tempList.append(nums[i])
        used[i] = True
        # explore via dfs
        backtrack(result_list, tempList, nums, used)
        # remove the candidate
        used[i] = False
        tempList.pop()


def permutation_dup(nums):
    result_list = []
    nums = sorted(nums)
    used = [False for _ in nums]
    backtrack(result_list, [], nums, used)
    return result_list


print(permutation_dup([1, 1, 2]))
vs.make_animation("images/permutation_dup.gif", delay=2)
