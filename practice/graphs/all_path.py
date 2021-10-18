solution = []


def all_path(graph, src, dst, solution, seen=set()):
    #! Do calculation here.

    solution += src
    if src == dst:
        print(f'solution -> {solution}')
        return True

    # If the src node is in visited set, return to avoid cycles.
    if str(src) in seen:
        return

    # We're converting src to str to maintain consistency.
    seen.add(str(src))

    for neighbor in graph[src]:
        all_path(graph, neighbor, dst, solution, seen)
