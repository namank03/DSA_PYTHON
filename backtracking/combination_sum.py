def backtrack(result_list, tempList, nums, target):
    # Add condition here to validate the state before adding it to the result list
    if target == 0:
        print(f'tempList[:] -> {tempList[:]}')
        result_list.append(tempList[:])

    if target < 0:
        return

    for i in range(len(nums)):
        tempList.append(nums[i])
        backtrack(result_list, tempList,  nums[i:], target - nums[i])
        tempList.pop()


def combination_sum(nums, target):
    result_list = []
    nums = sorted(nums)
    backtrack(result_list, [], nums, target)
    return result_list


a = [2, 1, 3, 4]
t = 8

res = combination_sum(a, t)
print(f'res -> {res}')
