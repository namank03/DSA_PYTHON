def backtrack(result_list, tempList, nums):
    # Add condition here to validate the state before adding it to the result list

    result_list.append(tempList[:])
    for i in range(len(nums)):
        # add condition here to make sure the current candidate is a valid candidate

        tempList.append(nums[i])
        # explore via dfs, here we have diff options to pass nums - 1) explore next elements nums[i+1:] 2)- expore next elements including current nums[i:] 3) - remove the current element and explore the rest - nums[:i] + nums[i+1:]
        backtrack(result_list, tempList, nums[i+1:])
        # remove the candidate
        tempList.pop()


def main_func(nums):
    result_list = []
    nums = sorted(nums)
    backtrack(result_list, [], nums)
    return result_list
