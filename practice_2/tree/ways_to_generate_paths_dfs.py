class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.left = b
a.right = c

b.left = d

c.left = e
c.right = f


def lca(root, node1, node2):
    def get_path(root, node, path=[]):
        if root:
            if root == node:
                return path + [root]
            return get_path(root.left, node, path + [root]) or get_path(
                root.right, node, path + [root]
            )

    a = get_path(root, node1)
    b = get_path(root, node2)

    print(f'a -> {a}')
    print(f'b -> {b}')


lca(a, e, f)


def lca2(root, node1, node2):
    def get_path(root, node):
        if root:
            if root == node:
                return [root]
            res = get_path(root.left, node) or get_path(root.right, node)
            if res:
                return [root] + res

    a = get_path(root, node1)
    b = get_path(root, node2)

    print(f'a -> {a}')
    print(f'b -> {b}')
