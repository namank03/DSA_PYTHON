
from visualiser.visualiser import Visualiser as vs

result_list = []


@vs(node_properties_kwargs={"shape": "record", "color": "#f57542", "style": "filled", "fillcolor": "grey"})
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
vs.make_animation("images/backtrack2.gif", delay=2)
print(result_list)
