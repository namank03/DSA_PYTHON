graph = {1: [2], 2: [1], 4: [6], 5: [6], 7: [6], 8: [6], 6: [4, 5, 7, 8], 3: []}


def traverse(graph, src, seen):
    if src in seen:
        return False
    seen.add(src)
    for neighbor in graph[src]:
        traverse(graph, neighbor, seen)
    return True


def connectedComponentsCount(graph):
    seen = set()
    return sum(traverse(graph, node, seen) for node in graph)


count = connectedComponentsCount(graph)
print(count)
