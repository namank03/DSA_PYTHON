# * Here we are further optimizing the haspath with the seen array. If the node is traversed before and the path is not found, So there is no need to traverse the node again and we can safely move to the next neighour in line
import snoop


def cache(func):
    d = {}

    def wrapper(*args):
        try:
            return d[args]
        except KeyError:
            result = d[args] = func(*args)
            return result

    return wrapper


@snoop
def exploreDepthFirst(graph, i, j, seen):

    # * TIP: When you're dealing with square/rectangle traversal is better to evaluate the inbound 1st and return early. This will gonna make sure that we're not traversing out of the square/rectangle at any point of time

    rowInbound = 0 <= i < len(graph)
    colInbound = 0 <= j < len(graph[0])
    if not rowInbound or not colInbound:
        return 0

    if graph[i][j] == 'w':
        return 0

    if (i, j) in seen:
        return 0

    seen.add((i, j))

    size = 1
    size += exploreDepthFirst(graph, i - 1, j, seen)
    size += exploreDepthFirst(graph, i + 1, j, seen)
    size += exploreDepthFirst(graph, i, j - 1, seen)
    size += exploreDepthFirst(graph, i, j + 1, seen)

    return size


def islandCount(graph):
    seen = set()
    min_size = 100
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            island_size = exploreDepthFirst(graph, i, j, seen)
            if island_size < min_size and island_size != 0:
                min_size = island_size

    return min_size


graph = [
    ['w', 'w', 'w', 'l'],
    ['w', 'l', 'l', 'w'],
    ['w', 'l', 'w', 'l'],
    ['l', 'l', 'w', 'l'],
]


print(islandCount(graph))
