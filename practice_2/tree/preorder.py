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


def preorder(root):
    if root:
        print(root, end='')
        preorder(root.left)
        preorder(root.right)


preorder(a)


def in_order(root):
    if root:
        in_order(root.left)
        print(root, end='')
        in_order(root.right)


in_order(a)
