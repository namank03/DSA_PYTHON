matrix = [
    [3, 30, 38],
    [36, 43, 60],
    [40, 51, 69],
]


def solve(matrix, n, m):
    l, r = 0, n * m
    mid = (l + r) // 2
    mid_i, mid_j = divmod(mid, n)


solve(matrix, 3, 3)
