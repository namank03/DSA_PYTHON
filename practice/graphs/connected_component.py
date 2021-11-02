from visualiser.visualiser import Visualiser as vs

edge_list = [
    (1, 0),
    (1, 2),
    (3, 4)
]


def create_graph(edge_list):
    graph = {}
    for node1, node2 in edge_list:
        graph[node1] = graph.get(node1, [])
        graph[node1].append(node2)
        graph[node2] = graph.get(node2, [])
        graph[node2].append(node1)

    return graph


graph = create_graph(edge_list)
print(f'graph -> {graph}')


def explore(graph, node, seen):
    if node is None:
        return False

    if node in seen:
        return False

    seen.add(node)

    c = 1
    for neighbor in graph[node]:
        c += 1
        explore(graph, neighbor, seen)

    return c


def connected_componet(graph):
    seen = set()
    return sum(explore(graph, i, seen) for i in graph)


res = connected_componet(graph)

print(f'res -> {res}')
