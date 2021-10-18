
def helper(graph_matrix):
    d = {}
    for i in range(len(graph_matrix)):
        for j in range(len(graph_matrix[0])):
            if i == j:
                continue
            d[i] = d.get(i, [])
            if graph_matrix[i][j] == 1:
                d[i].append(j)

    return d


def depthFirstTraverse(graph, src, seen=set()):
    # If the element is seen before we return False. This Can be used to detect cycle and optimize graph performance
    if str(src) in seen:
        return False
    # If the element is not in the set then we add it.
    seen.add(str(src))
    for neighbor in graph[src]:
        depthFirstTraverse(graph, neighbor, seen)

    return True


isConnected = [[1]]
graph = helper(isConnected)
print(graph)
sum(depthFirstTraverse(graph, i) for i in range(len(graph)))
