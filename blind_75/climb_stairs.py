# * At a time we can take either 1 or 2 steps. If n == 1 then there's only one way. Else if n > 1 then there's a choice. Seems like we can use n == 1 as our base case.
from functools import lru_cache


@lru_cache(None)
def climbStairs(n):

    if n in [0, 1]:
        return 1

    return climbStairs(n-1) + climbStairs(n-2)
