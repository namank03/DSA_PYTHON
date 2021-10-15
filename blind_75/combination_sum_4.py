class Solution:
    def combinationSum4(self, nums, target: int) -> int:

        def solve(nums, target, memo={}):
            if target == 0:
                return True

            if target < 0:
                return False

            if target in memo:
                return memo[target]

            memo[target] = sum(solve(nums, target-i) for i in nums)
            return memo[target]

        return solve(nums, target)
