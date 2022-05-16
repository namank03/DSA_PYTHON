class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

tree = TreeNode(1)
node2 = TreeNode(2)
node3 =  TreeNode(3)
node4 =  TreeNode(4)
node5 =  TreeNode(5)
node6 =  TreeNode(6)
node7 =  TreeNode(7)

tree.left = node2
tree.right = node3
node2.left =  node4
node2.right = node5
node3.left = node7
node3.right = node6

def inorder(node):
    if not node: return
    inorder(node.left)
    print(node.val, end =" ")
    inorder(node.right)
    
inorder(tree)


# left view
res = []
def left_view(root, level, res):
    if not root: return
    if level == len(res):
        res.append(root.val)
    left_view(root.left, level +1, res)
    left_view(root.right, level +1, res)

left_view(tree, 0, res)
print(res)



# left view
res = []
def right_view(root, level, res):
    if not root: return
    if level == len(res):
        res.append(root.val)
    right_view(root.right, level +1, res)
    right_view(root.left, level +1, res)
    
right_view(tree, 0, res)
print(res)

minMax = [float('inf'), - float('inf')]
def width(root, hl, minMax):
    if not root: return
    minMax[0] = min(minMax[0], hl)
    minMax[1] = max(minMax[1], hl)
    if root.left: width(root.left, hl - 1, minMax)
    if root.right: width(root.right, hl + 1, minMax)

width(tree, 0, minMax)
print('minmax', minMax)


def bottomView(root):
    # base case
    if not root: return
    width(tree, 0, minMax)
    w = minMax[1] - minMax[0] + 1
    ans = [0] * w
    queue = [(tree, abs(minMax[0]))]
    while queue:
        size = len(queue)
        while size > 0:
            node, hl = queue.pop(0)
            ans[hl] = node.val
            if node.left: queue.append((node.left, hl -1))
            if node.right: queue.append((node.right, hl +1))
            size -=1
    return ans
ans = bottomView(tree)
print('bottom view', ans)





def topView(root):
    # base case
    if not root: return
    width(tree, 0, minMax)
    w = minMax[1] - minMax[0] + 1
    print(w)
    ans = [None] * w
    queue = [(tree, abs(minMax[0]))]
    while queue:
        size = len(queue)
        while size > 0:
            node, hl = queue.pop(0)
            if ans[hl] is None:
                ans[hl] = node.val
            if node.left: queue.append((node.left, hl -1))
            if node.right: queue.append((node.right, hl +1))
            size -=1
    return ans
ans = topView(tree)
print('top view', ans)