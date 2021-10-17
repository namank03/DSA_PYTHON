

graph = {'a': ['c', 'b'], 'b': ['d'], 'c': [
    'e'], 'd': ['f'], 'e': ['a'], 'f': []}


def depthFirst(graph, source):
    # here if the graph[source] is empty List in that case - No recursive call is made and we'll simply return(Base Case)
    for neighbor in graph[source]:
        depthFirst(graph, neighbor)


depthFirst(graph, 'a')
