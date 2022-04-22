grid = [
    ['', 'w', ''],
    ['', '', 'w'],
    ['', '', 'w'],
    ['w', '', ''],
]

sx, sy = (3, 2)
dx, dy = (0, 0)


def can_reach_target(grid, sx, sy, dx, dy, visited=set()):
    if (
        sx < 0
        or sx >= len(grid)
        or sy < 0
        or sy >= len(grid[0])
        or (sx, sy) in visited
        or grid[sx][sy] == 'w'
    ):
        return False

    if sx == dx and sy == dy:
        return True

    visited.add((sx, sy))
    min_ans = float('inf')
    for mx, my in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        while (
            sx + mx < len(grid)
            and sx + mx >= 0
            and sy + my < len(grid[0])
            and sy + my >= 0
            and grid[sx + mx][sy + my] != 'w'
        ):
            sx += mx
            sy += my
        if tmp_ans := can_reach_target(grid, sx, sy, dx, dy, visited):
            tmp_ans += 1
            min_ans = min(min_ans, tmp_ans)
    return min_ans


res = can_reach_target(grid, sx, sy, dx, dy)
print(f'res -> {res}')
