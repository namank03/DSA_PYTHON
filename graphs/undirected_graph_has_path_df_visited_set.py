from helper_edge_list_to_adjacency_list import create_adjacency_list

edge_list = [['i', 'j'], ['k', 'i'], ['m', 'k'], ['k', 'l'], ['o', 'n']]


def hasPathDF(graph, src, dst, visited_set):
    if src == dst:
        return True
    visited_set.add(src)

    return any(
        hasPathDF(graph, neighbor, dst, visited_set)
        for neighbor in graph[src]
        if neighbor not in visited_set
    )


def check_path(edge_list, node1, node2):
    graph = create_adjacency_list(edge_list)
    return hasPathDF(graph, node1, node2, set())


print(check_path(edge_list, 'i', 'l'))
