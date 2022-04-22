arr = [[6, 9], [8, 10], [1, 2], [1, 5], [13, 15]]
# ans = [[1,5], [6,15]]


def merge_interval(arr):
    arr.sort(key=lambda x: x[0])
    res = [arr[0]]
    for i in range(len(arr) - 1):
        if res[-1][1] >= arr[i + 1][0]:
            interval = res.pop()
            res.append([interval[0], arr[i + 1][1]])
        else:
            res.append(arr[i + 1])

    return res


res = merge_interval(arr)

print(f'res -> {res}')


# topological sort
# def topological_sort(graph):
#

graph = {0: [1], 1: [0]}


def dfs(graph):
    visited = set()

    def dfs_util(node):
        if node in visited:
            return
        visited.add(node)
        for n in graph.get(node, []):
            dfs_util(n)

    for node in graph:
        dfs_util(node)


dfs(graph)

# topological sort in python


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


# detect cycle top sort in python
def detect_cycle(graph):
    visited = set()
    stack = []

    def dfs_util(node):
        if node in visited:
            return True
        visited.add(node)
        stack.append(node)
        for n in graph.get(node, []):
            if dfs_util(n):
                return True
        stack.pop()
        return False

    for node in graph:
        if dfs_util(node):
            return True
    return False
