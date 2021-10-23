import snoop

graph = [[1, 2, 1], [2, 3, 2], [1, 3, 2]]


def helper(graph):
    d = {}
    for i, j, k in graph:
        d[i] = d.get(i, [])
        d[i].append((j, k))
        d[j] = d.get(j, [])

    return d


graph = helper(graph)
print(f'graph -> {graph}')


@snoop
def depthFirstTraverse(graph, src, seen=set()):
    # If the element is seen before we return False. This Can be used to detect cycle and optimize graph performance
    if str(src) in seen:
        return 0
    # If the element is not in the set then we add it.
    seen.add(str(src))

    for neighbor, cost in graph[src]:
        total_running_cost = 0
        total_running_cost += cost + depthFirstTraverse(graph, neighbor, seen)
        max_cost = total_running_cost

    return max_cost


seen = set()
result = depthFirstTraverse(graph, 2, seen)
if len(graph) == len(seen):
    print(f'result -> {result}')
