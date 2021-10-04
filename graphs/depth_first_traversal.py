graph = {'a': ['c', 'b'], 'b': ['d'], 'c': ['e'], 'd': ['f'], 'e': [], 'f': []}


def depthFirst(graph, source):
    stack = [source]
    while stack:
        current = stack.pop()
        print(current, end=',')
        for val in graph[current]:
            stack.append(val)


depthFirst(graph, 'a')
