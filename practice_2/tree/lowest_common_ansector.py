graph = {
    1: [2, 3],
    2: [4, 5],
    5: [6],
    4: [8],
    3: [7],
    7: [],
    6: [],
    8: [],
}

node1 = 8
node2 = 7


def lca(root, node1, node2):
    def get_path(src, dst):
        if src == dst:
            return [src]
        for neighbor in graph[src]:
            res = get_path(neighbor, dst)
            #! early return.. Remember to use return statement inside if condition for an early return.!!
            if res is not None:
                return res + [src]

    b = get_path(root, node2)
    a = get_path(root, node1)

    print(f'a -> {a}')
    print(f'b -> {b}')
    if a and b:
        pass


lca(1, node1, node2)
