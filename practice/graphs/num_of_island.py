
def num_island(a):

    seen = set()
    count = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if explore(a, i, j, seen):
                count += 1

    return count


def explore(graph, i, j, seen):

    rowInbound = 0 <= i < len(graph)
    colInbound = 0 <= j < len(graph[0])

    if not rowInbound or not colInbound:
        return False

    if graph[i][j] in seen:
        return False

    explore(graph, i+1, j, seen)
    explore(graph, i, j + 1, seen)
    explore(graph, i-1, j, seen)
    explore(graph, i, j-1, seen)
