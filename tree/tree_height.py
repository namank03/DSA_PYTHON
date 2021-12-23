tree = {
    1: [3, 5],
    3: [7, 2],
    5: [6, 90, 100],
    6: [67],
}


def tree_height(root):
    if root is None:
        return 0

    if len(tree.setdefault(root, [])) == 0:
        return 1

    #  return the height of the left subtree and the right subtree and then add 1 to the height.
    return 1 + max(tree_height(child) for child in tree[root])


res = tree_height(1)
print(f'res -> {res}')
