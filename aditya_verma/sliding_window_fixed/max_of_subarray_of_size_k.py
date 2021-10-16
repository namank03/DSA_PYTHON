import math

import snoop


@snoop
def max_subarray_k(nums, k):
    i = j = 0
    g_r = []
    c_r = []

    while j < len(nums):

        # *if we found the element at index j which is greater than the last element of the c_r. Then we can empty the list and index that element. Else, we can just keep adding the 2nd/3rd.. max as they may come in use later. Remember adding to c_r calculations are done at the start.
        while c_r and c_r[-1] < nums[j]:
            c_r.pop()
        c_r.append(nums[j])

        # moving window
        if j-i+1 < k:
            j += 1

        elif j-i+1 == k:

            # * Max element is always present at the start so we can append this to global result.
            g_r.append(c_r[0])

            # *  if the num at index i is equal to the 1st element of c_r. We need to remove the element as for the next iteration we can't use the same element. Remember cal to remove the element or at the start of the window are done here.
            if nums[i] == c_r[0]:
                c_r.pop(0)

            j += 1
            i += 1

    return g_r


print(max_subarray_k([1, 3, 1, 2, 0, 5], 3))
