# Root is a node with no parent, while the leaf node is the node with no children.
# ! Binary tree characteristics are -
# * Binary tree is a tree with at most 2 children per node, and only one node. There's exist only 1 path from the root to any node(Meaning if there's a cycle then it's not a binary tree).
#! Edge case - Empty tree is also considered as a binary tree.

# Programmatic representation of the binary tree -

import snoop


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
b.left = d
c.left = e

# One way to traverse a tree is to use dfs. for this we'll need a stack.
# Programmatic representation depth first traversal of binary tree using stack


def dfs(root):
    #! Guard condition for the empty tree
    if root is None:
        return

    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val, end=',')
        if node.left != None:
            stack.append(node.left)
        if node.right != None:
            stack.append(node.right)


print()


# Generate the path via dfs
def dfs_path(root):
    #! Guard condition for the empty tree
    if root is None:
        return
    path = []

    stack = [root]
    while stack:
        node = stack.pop()
        path.append(node.val)
        print(node.val, end=',')
        if node.left != None:
            stack.append(node.left)
        if node.right != None:
            stack.append(node.right)

    return path


# No need to handle the guard condition in the recursive version.


def dsf_recursive(root):
    if root is None:
        return
    print(root.val, end=',')
    dsf_recursive(root.left)
    dsf_recursive(root.right)


# We can do the slight variation in the recursive call to generate the path.

def dsf_path_recursive(root):
    if root is None:
        return []
    left_result = dsf_path_recursive(root.left)
    right_result = dsf_path_recursive(root.right)
    return [root.val] + left_result + right_result


print(dsf_path_recursive(a))


# * bfs version using queue

def bfs(root):
    #! Guard condition for the empty tree
    if root is None:
        return

    path = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        path.append(node.val)
        print(node.val, end=', ')
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
    return path


bfs(a)
