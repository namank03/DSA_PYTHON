
# from visualiser.visualiser import Visualiser as vs
from functools import lru_cache


def lps(s):
    @lru_cache(None)
    def dp(s1, start, end):
        if start < 0 or end >= len(s1):
            return 0

        if s1[start] == s1[end]:
            return 2 + dp(s1, start-1, end+1)
        else:
            return 0

    return max(max(dp(s, i, i) - 1, dp(s, i, i+1)) for i in range(len(s)))


print(lps('cabbaccaaabaaa'))
