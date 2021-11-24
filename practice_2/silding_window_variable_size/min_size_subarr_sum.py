import math


def min_size_subarr_sum(target, nums):
    i = j = 0
    g_r = 100
    c_r = 0

    while j < len(nums):
        c_r += nums[j]

        if c_r >= target:
            while c_r > target:
                g_r = min(j-i+1, g_r)
                c_r -= nums[i]
                i += 1

            if c_r == target:
                c_r -= nums[j]
                continue

        j += 1

    return g_r


print(min_size_subarr_sum(11,  [1, 2, 3, 4, 5]))
