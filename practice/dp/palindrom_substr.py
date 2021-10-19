from functools import lru_cache

import snoop


def lps(s):
    @lru_cache(None)
    def dp(left, right):
        if left < 0 or right == len(s):
            return 0

        if s[left] == s[right]:
            return 1 + dp(left-1, right+1)

        else:
            return 0

    return sum(dp(i, i) for i in range(len(s))) + sum(dp(i, i+1) for i in range(len(s)))


print(lps('aaa'))
