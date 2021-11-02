import queue


def gen_parenthesis(n):
    def solve(o, c, op=""):
        if o == 0 and c == 0:
            print(f'op -> {op}')

        if o < 0 or c < 0 or c < o:
            return

        solve(o-1, c, op+'(')
        solve(o, c-1, op+')')

    solve(n, n)


gen_parenthesis(3)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')

a.left = b
a.right = c
c.left = d
c.right = e


def dfs(root):
    if root is None:
        return 0

    return max(1 + dfs(root.left), 1 + dfs(root.right))


res = dfs(a)
print(f'res -> {res}')


def bfs(root):
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(f'node -> {node.val}')
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


bfs(a)
