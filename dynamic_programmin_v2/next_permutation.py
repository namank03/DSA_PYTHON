# Algorithm here - https://www.nayuki.io/page/next-lexicographical-permutation-algorithm


# def next_permutation(nums):
#     i = 0
#     pivot = 0
#     # * 1t step is to get the pivot and divide the array into 2 half's.
#     while i < len(nums):
#         if nums[i] < nums[i+1]:
#             i += 1
#         else:
#             pivot = i
#             break

#     # * Find next greatest element in the right array starting from the right direction.
#     for i in range(len(nums)-1, pivot - 1, -1):
#         if nums[i] > nums[pivot-1]:
#             nums[i], nums[pivot-1] = nums[pivot-1], nums[i]
#             nums = nums[:pivot] + nums[pivot:][::-1]
#             break

#     return nums


# next_permutation([0, 1, 2, 5, 3, 3, 0])
