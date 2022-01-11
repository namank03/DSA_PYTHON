import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = word


def dfs(board, node, i, j, res):
    if node.isWord:
        res.append(node.isWord)
        node.isWord = False
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return
    tmp = board[i][j]
    node = node.children.get(tmp)
    if not node:
        return
    board[i][j] = "#"
    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        dfs(board, node, i + x, j + y, res)
    board[i][j] = tmp


def findWords(board, words):
    res = []
    trie = Trie()
    node = trie.root
    for w in words:
        trie.insert(w)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] in node.children:
                dfs(board, node, i, j, res)
    return res


board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"],
    ["e", "a", "t", "v"],
]

words = ["oath", "pea", "eat", "rain"]


res = findWords(board, words)
print(f'res -> {res}')
