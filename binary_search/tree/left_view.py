class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# left view of a binary tree
# Given a binary tree, return the left view of it.

def left_view(self, root):
    if not root:
        return []
    res = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        # Notice this condition
        if not queue:
            res.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res


# left view using dfs
def left_view_dfs(root):
    if not root:
        return []
    res = []
    def dfs(root, level, res):
        if not root:
            return
        # Notice this condition
        if len(res) == level:
            res.append(root.val)
        dfs(root.left, level+1, res)
        dfs(root.right, level+1, res)
    dfs(root, 0, res)
    return res


# right view using dfs
def right_view_dfs(root):
    if not root:
        return []
    res = []
    def dfs(root, level, res):
        if not root:
            return
        # Notice this condition
        if len(res) == level:
            res.append(root.val)
        # Notice the change here
        dfs(root.right, level+1, res)
        dfs(root.left, level+1, res)

# rigth view using bfs
def right_view_bfs(root):
    if not root:
        return []
    res = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        # Notice this condition
        if len(res) == len(queue):
            res.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res
