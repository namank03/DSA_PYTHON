from collections import defaultdict
from functools import reduce


def create_trie(words):
    _trie = lambda: defaultdict(_trie)
    trie = _trie()
    for w in words:
        reduce(dict.__getitem__, w, trie)['_end'] = w
    return trie


board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"],
    ["e", "a", "t", "v"],
]

words = ["oath", "pea", "eat", "rain"]


def dfs(board, i, j, node, res):
    if "_end" in node:
        print('h')
        res.append(node["_end"])
        node['_end'] = False
        return

    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return

    tmp = board[i][j]
    node = node[tmp]

    if not node:
        return

    board[i][j] = "#"

    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        dfs(board, i + x, i + y, node, res)

    board[i][j] = tmp


def findWords(board, words):
    res = []
    trie = create_trie(words)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] in trie:
                dfs(board, i, j, trie, res)

    return res


res = findWords(board, words)
print(f'res -> {res}')
