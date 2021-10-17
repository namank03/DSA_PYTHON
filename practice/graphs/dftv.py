def depthFirstTraverse(graph, src, seen=set()):
    # If the element is seen before we return False. This Can be used to detect cycle and optimize graph performance
    if str(src) in seen:
        return False
    # If the element is not in the set then we add it.
    seen.add(str(src))
    print(src, end=", ")
    for neighbor in graph[src]:
        depthFirstTraverse(graph, neighbor, seen)
    return True


graph = {'a': ['c', 'b'], 'b': ['d'], 'c': [
    'e'], 'd': ['f'], 'e': ['a'], 'f': []}
depthFirstTraverse(graph, 'a')
