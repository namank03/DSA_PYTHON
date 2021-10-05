graph = {'a': ['c', 'b'], 'b': ['d'], 'c': ['e'], 'd': ['f'], 'e': [], 'f': []}


def breadthFirstTraversal(graph, source):
    queue = [source]
    while queue:
        current = queue.pop(0)
        print(current, end=' ')
        for neighbor in graph[current]:
            queue.append(neighbor)


breadthFirstTraversal(graph, 'a')
