def prod_arr_es(nums):
    # ! Here, the trick is to keep 2 array prefix and postfix
    prefix = [1] * len(nums)
    postfix = [1] * len(nums)

    for i in range(len(nums)-1):
        prefix[i + 1] = prefix[i] * nums[i]

    n = len(nums)
    for i in range(len(nums)-1):
        postfix[n - (i + 2)] = postfix[n - (i+1)] * nums[n - (i+1)]

    for i in range(len(nums)):
        nums[i] = prefix[i]*postfix[i]

    return nums


prod_arr_es([2, 3, 4, 2])
