graph = {'w': ['x', 'v'], 'x': ['y'], 'y': ['z'], 'v': ['z']}


def findShortestDistance(graph, source, destination):
    queue = [(source, 0)]
    # ! NOTE:  Here we're initializing the visited set with the source node following the same principle whatever goes inside the queue must be marked as visited.
    visited = {source}
    while queue:
        current, current_dist = queue.pop(0)
        if current == destination:
            return current_dist
        current_dist += 1
        for neighbor in graph[current]:
            if neighbor not in visited:
                # just before adding the node to the queue we need to mark it as a visited. Everything that's going inside the queue means that we've visited that
                visited.add(neighbor)
                queue.append((neighbor, current_dist))

    # -1 means the there's no path between source and destination
    return -1


print(findShortestDistance(graph, 'w', 'z'))
