from functools import lru_cache

b = [0, 3, 2, 1, 0]


@lru_cache(maxsize=None)
def solve(a):
    # check if 1st element is 0
    if a[0] == 0 and len(a) == 1:
        return True

    if a[0] == 0 and len(a) > 1:
        return False

    if a[0] >= len(a) - 1:
        return True

    return any(solve(a[i:]) for i in range(a[0], 0, -1))


res = solve(tuple(b))
