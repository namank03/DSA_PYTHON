graph = {'a': ['c', 'b'], 'b': ['d'], 'c': ['e'], 'd': ['f'], 'e': [], 'f': []}


def depthFirst(graph, source):
    print(source, end=',')
    #! When the source node is e. There are no neighbors. Meaning, this condition can be utilized as the base case as there will be no recursive call in that case and function will simply print the "e" and return None
    for val in graph[source]:
        depthFirst(graph, val)


depthFirst(graph, 'a')
