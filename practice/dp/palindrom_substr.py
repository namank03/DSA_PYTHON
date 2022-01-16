from functools import lru_cache


def lps(s):
    @lru_cache(None)
    def dp(left, right):
        if left < 0 or right == len(s):
            return 0

        return 1 + dp(left - 1, right + 1) if s[left] == s[right] else 0

    return sum(dp(i, i) for i in range(len(s))) + sum(
        dp(i, i + 1) for i in range(len(s))
    )


print(lps('aaa'))
