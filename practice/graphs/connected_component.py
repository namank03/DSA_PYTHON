edge_list = [(1, 0), (1, 2), (3, 4)]


def create_graph(edge_list):
    graph = {}
    for node1, node2 in edge_list:
        graph.setdefault(node1, []).append(node2)
        graph.setdefault(node2, []).append(node1)
    return graph


graph = create_graph(edge_list)
print(f'graph -> {graph}')


def explore(graph, node, seen):
    if node is None:
        return False

    if node in seen:
        return False

    seen.add(node)

    return 1 + sum(explore(graph, neighbor, seen) for neighbor in graph[node])


def connected_componet(graph):
    seen = set()
    return sum(explore(graph, i, seen) for i in graph)


res = connected_componet(graph)

print(f'res -> {res}')
