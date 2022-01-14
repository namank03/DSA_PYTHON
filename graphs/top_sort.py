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


top_sort(graph)
