from itertools import accumulate


def max_sum(nums):

    # Here the trick is to use the kadan's algorithm. keep track of the running sum and update the max sum whenever the running sum goes greater than the max sum.

    max_sum = running_sum = nums[0]

    for i in nums[1:]:
        running_sum += i
        running_sum = max(running_sum, i)
        max_sum = max(max_sum, running_sum)

    return max_sum


def max_sum_via_acc(nums):
    return max(accumulate(nums, lambda a, b: max(b, a+b)))


print(max_sum([5, 4, -11, 7, 8]))
