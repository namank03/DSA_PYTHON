
def backtrack(result_list, tempList, nums):
    if len(tempList[:]) == 3:
        result_list.append(tempList[:])
    for i in range(len(nums)):
        tempList.append(nums[i])
        backtrack(result_list, tempList, nums[:i] + nums[i+1:])
        tempList.pop()


def subsets(nums):
    result_list = []
    nums = sorted(nums)
    backtrack(result_list, [], nums)
    return result_list


res = subsets([1, 2, 3])
print(f'res -> {res}')
