# edge_list = [['i', 'j'], ['k', 'i'], ['m', 'k'], ['k', 'l'], ['o', 'n']]


def create_adjacency_list(edge_list):
    graph = {}
    for node1, node2 in edge_list:
        graph[node1] = graph.get(node1, [])
        graph[node1].append(node2)
        graph[node2] = graph.get(node2, [])
        graph[node2].append(node1)

    return graph


# {'i': ['j', 'k'], 'j': ['i'], 'k': ['i', 'm', 'l'], 'm': ['k'], 'l': ['k'], 'o': ['n'], 'n': ['o']}
