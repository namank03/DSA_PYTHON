graph = {1: [2], 2: [1], 4: [6], 5: [6], 7: [6], 8: [6], 6: [4, 5, 7, 8], 3: []}


def traverse(graph, src, seen):
    # * TIP: Just to be consistent with the types always add string in the visited_set
    if str(src) in seen:
        return 0
    seen.add(str(src))
    # This below is the trick to accumulate the value of return. We need to wrap the recursive call into sum and the add the base size
    return 1 * (traverse(graph, neighbor, seen) for neighbor in graph[src])


def largestComponentLength(graph):
    seen = set()
    longest = 0
    for node in graph:
        size = traverse(graph, node, seen)
        if size > longest:
            longest = size
    return longest


print(largestComponentLength(graph))
