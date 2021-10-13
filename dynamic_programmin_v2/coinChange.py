
# def solve(coins, amount, memo={}):

#     if amount < 0:
#         return None

#     if amount == 0:
#         return 0

#     if amount in memo:
#         return memo[amount]

#     best_len = None

#     for i in coins:
#         count = solve(coins, amount-i, memo)
#         if count is not None:
#             count += 1
#             if best_len is None or best_len > count:
#                 best_len = count

#     memo[amount] = best_len
#     return best_len


# print(solve([2], 3))


class Solution:
    def solve(self, coins, amount, memo={}):

        if amount < 0:
            return None

        if amount == 0:
            return 0

        if amount in memo:
            return memo[amount]

        best_len = None

        for i in coins:
            count = self.solve(coins, amount-i, memo)
            if count is not None:
                count += 1
                if best_len is None or best_len > count:
                    best_len = count

        memo[amount] = best_len
        return memo[amount]

    def coinChange(self, coins, amount: int, memo={}) -> int:
        op = self.solve(coins, amount)
        if op is None:
            return -1
        return op


s = Solution()
print(s.coinChange([2], 3))
