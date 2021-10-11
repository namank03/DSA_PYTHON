
def canJump(nums) -> bool:
    if len(nums) <= 1:
        return True

    if nums[0] == 0:
        return False

    return any(canJump(nums[i:]) for i in range(nums[0], 0, -1))


canJump([2, 3, 2, 3, 1, 9, 3, 1, 2, 4, 2, 2,
         1, 5, 0, 3, 2, 2, 0, 0])
