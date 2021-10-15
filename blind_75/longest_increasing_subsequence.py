# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4

def solve(nums, n, memo={}):

    if n < 2:
        return 1

    if n in memo:
        return memo[n]

    # Here we're comparing the element n-1(last) with n-2(second last) if the condition matches we've got 2 choices i.e either to take the element or to not and we need the max of the result

    if nums[n-1] > nums[n-2]:
        memo[n] = max(1 + solve(nums, n-1, memo), solve(nums, n-1, memo))
    else:
        memo[n] = solve(nums, n-1, memo)

    return memo[n]


nums = [4, 10, 4, 3, 8, 9]
solve(nums, len(nums))
