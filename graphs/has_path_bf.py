graph = {
    'a': ['d'],
    'd': ['k', 'f'],
    'l': ['d'],
    'f': ['o'],
    'g': ['f'],
    'o': ['n'],
    'k': ['h', 'o'],
    'h': [],
    'n': [],
}


def hasPathBF(graph, source, destination):
    queue = [source]
    while queue:
        current = queue.pop(0)
        if current == destination:
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False


print(hasPathBF(graph, 'a', 'g'))
