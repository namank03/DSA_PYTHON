graph = {
    'f': [],
    'd': ['e'],
    'e': ['d'],
    'b': ['e', 'c'],
    'c': ['f'],
    'a': ['b', 'c'],
}


def top_sort(graph):
    visited = set()

    def dfs(node, path):
        if node in visited:
            return
        visited.add(node)
        path.append(node)
        for neighbor in graph[node]:
            dfs(neighbor, path)
        return path

    for node in graph:
        if node not in visited:
            res = dfs(node, [])
            print(f'res -> {res}')


res = top_sort(graph)
print(f'res -> {res}')


# top sort python
def top_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        if node in visited:
            return

        visited.add(node)

        for next_node in graph[node]:
            dfs(next_node)
        # append node after exploring
        stack.append(node)

    for node in graph:
        dfs(node)

    return stack[::-1]


res = top_sort(graph)
print(f'res -> {res}')


def topological_sort(graph):
    visited = set()
    stack = []

    def dfs_util(node):
        if node in visited:
            return
        visited.add(node)
        for n in graph.get(node, []):
            dfs_util(n)
        stack.append(node)

    for node in graph:
        dfs_util(node)

    return stack[::-1]


res = topological_sort(graph)
print(f'res -> {res}')
