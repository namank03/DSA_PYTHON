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
r = Node('r')

a.left = b
a.right = c
b.left = d
c.left = e


def tree_include(root, target):
    #! Guard condition for the empty tree
    if root is None:
        return False

    queue = [root]
    while queue:
        node = queue.pop(0)
        # some other calculations here
        if node.val == target.val:
            return True
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
    return False


# print(tree_include(a, r))


def tree_include_rec(root, target):
    if root is None:
        return False
    # Some other calculation for base cases. Ex - comparing the root val with the target val
    if root.val == target.val:
        return True
    return tree_include_rec(root.left, target) or tree_include_rec(root.right, target)


print(tree_include_rec(a, e))
