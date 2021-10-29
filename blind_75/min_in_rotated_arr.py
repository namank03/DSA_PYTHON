

def min_in_roteted_arr(nums):
    left, right = 0, len(nums) - 1

    while left < right:

        mid = (left + right) // 2

        # ! trick to check the pivot. if the element at mid position is greater than the element at right that means our array is rotated and the pivot is present to the right
        if nums[mid] > nums[right]:
            left = mid + 1

        #! if the mid is less then we check for if the rotation exists on the left side or not by shrinking the search space.
        else:
            right = mid

    return nums[left]


min_in_roteted_arr([4, 5, 6, 7, 0, 1, 2])
