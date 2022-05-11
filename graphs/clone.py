

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def dfs(node, visited):
    # if node is already visited, return the visited node
    if node in visited:
        return visited[node]
        # otherwise, create a new node and add it to the visited dict
    visited[node] = Node(node.val, [])
    # for each neighbor of the node
    for neighbor in node.neighbors:
        # recursively call dfs on the neighbor 
        # and add the returned node to the neighbors of the current node
        visited[node].neighbors.append(dfs(neighbor, visited))
    return visited[node]

# clone graph via dfs
def clone_graph(node):
    if not node:
        return None
    visited = {}
    return dfs(node, visited)
