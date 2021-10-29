from functools import lru_cache


@lru_cache(maxsize=None)
def test(a, l, r):
    if l >= r:
        return 0

    op = (min(a[l], a[r]) * (r - l))
    return max(op, test(a, l + 1, r), test(a, l, r - 1))


arr = [2, 1, 1, 2, 6]
m = test(tuple(arr), 0, len(arr)-1)
print(f'm -> {m}')
