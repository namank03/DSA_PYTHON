# 404 Sum of Left Leaves
def sum_of_left_leaves(self, root):
    if not root:
        return 0
    res = 0
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left:
            # if it's the left leaf, add it to the result
            if not node.left.left and not node.left.right:
                res += node.left.val
            else:
                queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res
