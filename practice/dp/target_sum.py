
from functools import lru_cache


@lru_cache(maxsize=None)
def solve(arr, target):
    if target == 0:
        return True

    if len(arr) == 0 or target < 0:
        return False

    return any(
        solve(arr[:i] + arr[i + 1:], target - arr[i]) for i in range(len(arr))
    )


a = [2, 23, 1, 5]
t = 8
res = solve(tuple(a), t)
print(f'res -> {res}')
