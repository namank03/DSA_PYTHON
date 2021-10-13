
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
