graph = [
    ['w', 'w', 'w', 'l'],
    ['w', 'l', 'l', 'w'],
    ['w', 'l', 'l', 'w'],
    ['l', 'l', 'w', 'l'],
]


def exploreDepthFirst(graph, i, j, seen):

    # * TIP: When you're dealing with square/rectangle traversal is better to evaluate the inbound 1st and return early. This will gonna make sure that we're not traversing out of the square/rectangle at any point of time

    rowInbound = 0 <= i < len(graph)
    colInbound = 0 <= j < len(graph[0])
    if not rowInbound or not colInbound:
        return False

    if graph[i][j] == 'w':
        return False

    if (i, j) in seen:
        return False

    seen.add((i, j))
    exploreDepthFirst(graph, i - 1, j, seen)
    exploreDepthFirst(graph, i + 1, j, seen)
    exploreDepthFirst(graph, i, j - 1, seen)
    exploreDepthFirst(graph, i, j + 1, seen)

    return True


def islandCount(graph):
    seen = set()
    count = 0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            count += exploreDepthFirst(graph, i, j, seen)

    return count


print(islandCount(graph))
