from collections import deque
# topological sort using khan's algo via indegree
graph = {
        1: [3],
        2: [3],
        3: [4,7],
        4: [5],
        7: [8],
        5: [6],
        6: [10],
        8 :[10],
        10: [],
    }

def topsort(graph):
    # set indegree to 0
    indegree = {u:0 for u in graph}
    # inc the indegree of the neighbours
    for u in graph:
        for v in graph[u]:
            indegree[v] +=1
    # put the node with indegree 0 in the queue
    queue = deque([u for u in indegree if indegree[u]==0])
    res = []
    while queue:
        u = queue.popleft()
        # add the node in res
        res.append(u)
        # decrease the indegree of the neighbours
        for v in graph[u]:
            indegree[v] -=1
            if indegree[v] == 0:
                queue.append(v)
        
    return res if len(res) == len(indegree) else []
    
        
res = topsort(graph)
print(res)