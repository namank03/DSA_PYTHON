word = "ABCGHDC"

grid = [
    ['A', 'B', 'C'],
    ['E', 'C', 'D'],
    ['D', 'G', 'H'],
]


def exist(board, word: str) -> bool:
    m, n = len(board), len(board[0])
    visited = set()  # Backtracting

    def dfs(i, j, visited, count):
        if count == len(word):
            return True
        if (
            i >= m
            or i < 0
            or j < 0
            or j >= n
            or (i, j) in visited
            or word[count] != board[i][j]
        ):
            return False
        visited.add((i, j))
        return any(
            dfs(i + dx, j + dy, visited, count + 1)
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]
        )

    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:  # Check at each position
                if dfs(i, j, visited, 0):
                    return True
    return False


res = exist(grid, word)
print(f'res -> {res}')
