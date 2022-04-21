def search_in_roteted_arr(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # ! trick to check the pivot. if the element at mid position is greater than the element at right that means our array is rotated and the pivot is present to the right
        if nums[mid] > nums[right]:
            left = mid + 1
        #! if the mid is less then we check for if the rotation exists on the left side or not by shrinking the search space.
        else:
            right = mid

    nums = nums[left:] + nums[:right]
    rotation = left

    left, right = 0, len(nums)

    found = False

    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            found = True
            break
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return (mid + rotation) % len(nums) if found else -1


print(search_in_roteted_arr([1], 1))
