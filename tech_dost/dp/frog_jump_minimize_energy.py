from functools import lru_cache

# Solve for 0 -> n
@lru_cache(maxsize=None)
def msolve(n):
    # base case 0 -> 0
    if n <= 0:
        return 0
    # do all possible solutions with index
    return min(
        abs(arr[n - 1] - arr[n]) + msolve(n - 1),
        abs(arr[n - 2] - arr[n]) + msolve(n - 2),
    )


arr = [10, 20, 30, 10]

# Tabulation
def tsolve(n):
    # init dp with n+1 if we're using 1 based indexing else we initialize with n
    dp = [-1] * (n)
    # base case 0
    dp[0] = 0
    # do all possible solutions with valid index -> here as we're using 0 based indexing the last valid index is n-1
    for i in range(1, n):
        dp[i] = min(
            abs(arr[n - 1] - arr[n]) + dp[i - 1],
            abs(arr[n - 2] - arr[n]) + dp[i - 2],
        )
    return dp[-1]


arr = [30, 10, 60, 10, 60, 50]

res = tsolve(len(arr) - 1)
print(f"res -> {res}")

#! everytime whenever there is i-1, i-2 in dp, there's always space optimization
# Tabulation with space optimization
def tosolve(n):
    # base case 0
    if n <= 0:
        return 0

    prev, prev2 = 0, 0
    # do all possible solutions with valid index -> here as we're using 0 based indexing the last valid index is n-1
    for _ in range(1, n):
        prev, prev2 = (
            min(
                abs(arr[n - 1] - arr[n]) + prev,
                abs(arr[n - 2] - arr[n]) + prev2,
            ),
            prev2,
        )
    return prev


arr = [30, 10, 60, 10, 60, 50]

res = tosolve(len(arr) - 1)
print(f"res -> {res}")

# everytime whenever there is i-1, i-2 in dp, there's always space optimization
