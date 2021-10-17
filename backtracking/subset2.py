
from visualiser.visualiser import Visualiser as vs

result_list = []


def backtrack(tempList, nums):
    if not nums:
        result_list.append(tempList[:])
    for i in range(len(nums)):
        tempList.append(nums[i])
        backtrack(tempList, nums[:i] + nums[i + 1:])
        tempList.pop()


def subsets(nums):
    nums = sorted(nums)
    backtrack([], nums)


subsets([1, 2, 3])
print(result_list)
