def minSubArrayLen(target, nums):
    # nums, target
    i = j = 0
    count = 0
    c_r = 0
    m_l = float('inf')

    while j < len(nums):
        c_r += nums[j]
        count += 1

        if c_r >= target:
            m_l = min(m_l, count)
            while c_r >= target:
                c_r -= nums[i]
                count -= 1
                i += 1
                if c_r >= target:
                    m_l = min(m_l, count)

        j += 1

    return m_l


target = 7
nums = [2, 3, 1, 2, 4, 3]
res = minSubArrayLen(target, nums)
print(f'res -> {res}')
