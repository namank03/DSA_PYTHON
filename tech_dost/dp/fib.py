from functools import lru_cache

# recurssive solution
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


# Memorization solution
@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


# Tabularisation
def fib(n):
    # init dp
    dp = [-1] * (n + 1)
    # write the base cases
    dp[0], dp[1] = 0, 1
    # write the for loop
    for i in range(2, n + 1):
        #  Copy the recurance
        dp[i] = dp[n - 1] + dp[n - 2]

    # TC -> O(N)
    # SC -> O(N)


# to further optimize this think what we need like for dp[i] we only need previous and 2nd previous. So, we can optimize space further

# Tabularisation with space optimization
def fib(n):
    # write the base cases
    prev, sec_prev = 0, 1
    # write the for loop
    for _ in range(2, n + 1):
        #  Copy the recurance
        ans = prev + sec_prev
        tmp = prev
        prev, sec_prev = ans, tmp

    print(ans)
    # TC -> O(N)
    # SC -> O(1)
