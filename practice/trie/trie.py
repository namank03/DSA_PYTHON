import itertools
from collections import defaultdict


class Node:
    def __init__(self):
        self.child = defaultdict(Node)
        self.is_word = False


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            node = node.child[w]
        node.is_word = True


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABC"


def dfs(board, node, i, j, res):
    if node.is_word:
        node.is_word = False
        return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return
    tmp = board[i][j]
    node = node.child.get(tmp)
    if not node:
        return
    board[i][j] = "#"
    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if dfs(board, node, i + x, j + y, res):
            return True
    board[i][j] = tmp
    return False


def exist(board, word: str) -> bool:
    if not board or not word:
        return False
    trie = Trie()
    for w in word:
        trie.insert(w)
    return any(
        dfs(board, trie.root, i, j, [])
        for i, j in itertools.product(range(len(board)), range(len(board[0])))
    )


res = exist(board, word)
print(res)
