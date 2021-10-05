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
def hasPathDF(graph, source, destination, seen):
    seen.add(source)
    # The below will serve as the base case
    if source == destination:
        return True
    for neighbor in graph[source]:
        if neighbor not in seen and hasPathDF(graph, neighbor, destination, seen):
            # ! TIP: We can include a if condition in the recursive call to return early here we're saying if one of the recursive call hit the base condition and returns true to the call stack that means we've found at least one of the path and we can exit the recursion now
            return True
    else:
        return False


graph = {
    'a': ['d'],
    'd': ['k', 'f'],
    'l': ['d'],
    'f': ['o'],
    'g': ['f'],
    'o': ['n'],
    'k': ['h', 'o'],
    'h': [],
    'n': [],
}


print(hasPathDF(graph, 'a', 'f', set()))


# *TIP:  seen/visited_set also helps us detecting/avoiding cycles in the undirected graphs
