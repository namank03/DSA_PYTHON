tree = {
    1: [3, 5],
    3: [7, 2],
    # 7: [],
    # 2: [],
    # 5: [],
}


def sum_leaf_node(root):

    # Base case when there's no node, empty tree..
    if root is None:
        return 0

    # base case when we only have one node..
    if len(tree.setdefault(root, [])) == 0:
        return root

    return sum(sum_leaf_node(child) for child in tree[root])


res = sum_leaf_node(1)
print(f'res -> {res}')
