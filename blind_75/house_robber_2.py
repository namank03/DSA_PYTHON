class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]

        def solve(nums, memo={}):
            if len(nums) == 1:
                return nums[0]

            if len(nums) < 1:
                return 0

            nums_str = "".join(map(str, nums))
            if nums_str in memo:
                return memo[nums_str]

            memo[nums_str] = max(nums[-1] + solve(nums[:-2], memo),
                                 solve(nums[:-1], memo))

            return memo[nums_str]

        return max(solve(nums[1:]), solve(nums[:-1]))
