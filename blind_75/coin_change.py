# Think of the smallest valid input ->
#! 1. Either we can have a no coin means the array is empty. If we have no coins then it's impossible to generate the required sum
#! 2. If the target sum is 0 then no coin is required to generate the required sum.

# * The above 2 will serve as the base condition and here we'll write the 2nd base condition 1st.
import math


def coin_change(coins, amount, memo={}):

    if amount == 0:
        return 0

    if len(coins) == 0 or amount < 0:
        return math.inf

    if amount in memo:
        return memo[amount]

    min_coins = math.inf

    for i in coins:
        result = coin_change(coins, amount-i, memo)
        if result != math.inf:
            result += 1
            if min_coins == math.inf or min_coins > result:
                min_coins = result

    memo[amount] = min_coins
    return min_coins


print(coin_change([2], 3))
# vs.make_animation('images/coinChange.gif', delay=2)
