# # topological sort easy solution with comments
# def topological_sort(graph):
#     def dfs(node, visited, stack, graph):
#         visited.add(node)
#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 dfs(neighbor, visited, stack, graph)
#         stack.append(node)

#     visited, stack = set(), []
#     for node in graph:
#         if node not in visited:
#             dfs(node, visited, stack, graph)
#     return stack[::-1]


# # 4.2.6 Bipartite Graph Check
# def is_bipartite(graph):
#     # check if graph is bipartite
#     def dfs(node, visited, color, graph):
#         visited.add(node)
#         for neighbor in graph[node]:
#             # if neighbor is not visited
#             if neighbor not in visited:
#                 dfs(neighbor, visited, color, graph)
#             # if neighbor is visited and color is same as current node
#             elif color[neighbor] == color[node]:
#                 return False
#         color[node] = not color[node]
#         return True
    
#     visited, color = set(), {}
#     for node in graph:
#         if node not in visited:
#             if not dfs(node, visited, color, graph):
#                 return False
#     return True


# Graph Edges Property Check via DFS Spanning Tree
def is_spanning_tree(graph):
    # check if graph is spanning tree
    def dfs(node, visited, graph):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited, graph)
    visited = set()
    for node in graph:
        if node not in visited:
            dfs(node, visited, graph)
    return len(visited) == len(graph)

# find stronglly connected_componets via tarjaan algorithm
