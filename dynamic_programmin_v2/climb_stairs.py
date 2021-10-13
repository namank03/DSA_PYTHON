
# def climb_stairs(n, memo={}):
#     if n < 0:
#         return False
#     if n == 0:
#         return True
#     if n in memo:
#         return memo[n]

#     memo[n] = climb_stairs(n-1) + climb_stairs(n-2)
#     return memo[n]


# print(climb_stairs(4))


class Solution:
    def solve(self, n, memo={}):
        if n < 0:
            return False
        if n == 0:
            return True
        if n in memo:
            return memo[n]

        memo[n] = self.solve(n-1) + self.solve(n-2)

        return memo[n]

    def climbStairs(self, n: int) -> int:
        return self.solve(n)
