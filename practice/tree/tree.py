class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root: Node) -> None:
        self.root = root

    def insert(self, val: int) -> None:
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node: Node, val: int) -> None:
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self._insert(node.left, val)
        elif node.right is None:
            node.right = Node(val)
        else:
            self._insert(node.right, val)

    def search(self, val: int) -> bool:
        return False if self.root is None else self._search(self.root, val)

    def _search(self, node: Node, val: int) -> bool:
        if node is None:
            return False
        elif node.val == val:
            return True
        elif val < node.val:
            return self._search(node.left, val)
        else:
            return self._search(node.right, val)

    def print_tree(self) -> None:
        def dfs(root):
            if root is None:
                return
            print(root.val, end='-')
            dfs(root.left)
            dfs(root.right)

        dfs(self.root)

    def left_view(self) -> None:
        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                collect(node.left, depth + 1)
                collect(node.right, depth + 1)

        view = []
        collect(self.root, 0)
        print(view)

    def right_view(self) -> None:
        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                collect(node.right, depth + 1)
                collect(node.left, depth + 1)

        view = []
        collect(self.root, 0)
        print(view)


tree = Tree(Node(5))
tree.insert(10)
tree.insert(3)
tree.insert(1)

tree.right_view()

# tree.print_tree()
tree.left_view()


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowest_common_ancestor(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'TreeNode':
        #  base case if root is in None  or either of the nodes p , q then it is a common ancestor return it
        if root in (None, p, q):
            return root
        # iterate for left and right subtree and save the result in left / right
        left, right = (
            self.lowest_common_ancestor(kid, p, q) for kid in (root.left, root.right)
        )
        # if we get the data from both left / right subtree then that root is a common ansestor. Otherwise, we need to return left / right subtree value
        return root if left and right else left or right
