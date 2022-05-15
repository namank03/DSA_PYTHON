# def max_subarray_k(nums, k):
#     i = j = 0
#     g_r = []
#     c_r = []

#     while j < len(nums):

#         # *if we found the element at index j which is greater than the last element of the c_r. Then we can empty the list and index that element. Else, we can just keep adding the 2nd/3rd.. max as they may come in use later. Remember adding to c_r calculations are done at the start.
#         while c_r and c_r[-1] < nums[j]:
#             c_r.pop()
#         c_r.append(nums[j])

#         # moving window
#         if j - i + 1 < k:
#             j += 1

#         elif j - i + 1 == k:

#             # * Max element is always present at the start so we can append this to global result.
#             g_r.append(c_r[0])

#             # *  if the num at index i is equal to the 1st element of c_r. We need to remove the element as for the next iteration we can't use the same element. Remember cal to remove the element or at the start of the window are done here.
#             if nums[i] == c_r[0]:
#                 c_r.pop(0)

#             j += 1
#             i += 1

#     return g_r


# print(max_subarray_k([1, 3, 1, 2, 0, 5], 3))


from collections import deque
def predictDays(day, k):
    # Write your code here
    i = j = 0
    res,g_r = [], []
    min_in_window = deque()
    win_size = (k<<1)+1
    while j < len(day):
        # moving window
        while min_in_window and min_in_window[-1] > day[j]:
            min_in_window.pop()
        min_in_window.append(day[j])
        if j - i + 1 < win_size:
            j += 1
        elif j - i + 1 == win_size:
            g_r.append(min_in_window[0])
            if (min_in_window[0] == day[((i+j)//2)]):
                res.append(((i+j)//2)+1)
            if day[i] == min_in_window[0]:
                min_in_window.popleft()
            j += 1
            i += 1
    return res, g_r


_, ans = predictDays([5,4,1,2,3,3,1,1,0,2,3], 5)
print(ans)



# Angry charles
def angry_charles(n, m, k, a, b):
    i = j = 0
    res = []
    while j < len(a):
        # moving window
        while i < j and a[i] <= a[j]:
            i += 1
        if i == j:
            j += 1
        elif i < j:
            res.append(a[i])
            j += 1
    return res


# kahn's algo top sort
def top_sort(graph):
    # initialize the in_degree of each node to 0
    in_deg = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            # Increase the indegree of each neighbor by 1
            in_deg[v] += 1
    # initialize the queue with all the nodes with 0 indegree
    q = deque([u for u in graph if in_deg[u] == 0])
    res = []
    while q:
        # pop the first node from the queue
        u = q.popleft()
        # add it to the result
        res.append(u)
        for v in graph[u]:
            # decrease the indegree of each neighbor by 1
            in_deg[v] -= 1
            # if the indegree of the neighbor becomes 0, add it to the queue
            if in_deg[v] == 0:
                q.append(v)
    if (res) == len(in_deg):
        return res
    else:
        return None



def top_sort(graph):
    # init the in degree to 0
    in_degree = {u: 0 for u in graph}
    for u in graph:
        # neigbour of u
        for v in graph[u]:
            in_degree[v] +=1
    
    queue = deque([u for u in graph if in_degree[u] == 0])
    res = []
    while queue:
        node = queue.popleft()
        res.append(node)
        # for each neighbour of node
        for v in graph[node]:
            # decrease the indegree of neighbor by 1
            in_degree[v] -=1
            if in_degree[v] == 0:
                queue.append(v)
    if len(res) == len(in_degree):
        return res
    else:
        return None


# union find algo

class UnionFind:
    def __init__(self,arr):
        self.arr = arr
        self.parent = [i for i in range(len(arr))]
        self.rank = [0] * len(arr)
    
    # Find and update parent
    def find(self,i):
        if self.parent[i] != i:
            # path compression by updating parent of i 
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    

    # perform union operation
    def union(self,i,j):
        i_id = self.find(i)
        j_id = self.find(j)
        # if both are in same set then we don't need to perform the union
        if i_id == j_id:
            return
        # check rank and and update the parent accordingly
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
            # if ranks are same then increment the rank of the parent
            if self.rank[i_id] == self.rank[j_id]:
                # parent j_id ko banaya hai to uski rank inc kardo agar initialily dono ki rank same thi to
                self.rank[j_id] += 1



# Create minimum spanning tree using dsu
def mst(graph):
    # create a dsu object
    dsu = UnionFind(graph)
    # sort the edges in increasing order of weight
    edges = sorted(graph.items(), key=lambda x: x[1])
    # initialize the result
    res = []
    # iterate over the edges
    for edge in edges:
        # get the vertices of the edge
        u, v = edge[0], edge[1]
        # if the vertices are not in the same set then perform union operation
        if dsu.find(u) != dsu.find(v):
            dsu.union(u,v)
            # add the edge to the result
            res.append(edge)
    return res

# modified bfs
def bfs(graph, s):
    # create a queue
    q = deque()
    # init the visited array
    visited = [False] * len(graph)
    # add the source to the queue
    q.append(s)
    # mark the source as visited
    visited[s] = True
    # init the distance array
    distance = [-1] * len(graph)
    # init the parent array
    parent = [-1] * len(graph)
    # init the distance of source to 0
    distance[s] = 0
    # init the parent of source to -1
    parent[s] = -1
    # iterate over the queue
    while q:
        # pop the first element from the queue
        u = q.popleft()
        # iterate over the neighbours of u
        for v in graph[u]:
            # if the neighbour is not visited then perform the bfs
            if not visited[v]:
                # mark the neighbour as visited
                visited[v] = True
                # add the neighbour to the queue
                q.append(v)
                # update the distance of neighbour
                distance[v] = distance[u] + 1
                # update the parent of neighbour
                parent[v] = u
    return distance, parent


def top_sort(graph):
    in_degree = {u:0 for u in  graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    
    queue = deque([u for u in graph if in_degree[u] == 0])
    res = []
    while queue:
        u = queue.popleft()
        res.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
        
    if len(res) == len(in_degree):
        return res
    else:
        return None

# Level order bfs
def level_order_bfs(grid):
    queue = deque()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                  grid[i][j] = -1                  
            else:
                queue.append((i,j))
    
    dirs = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
    while queue:
        i, j = queue.popleft()
        for x,y in dirs:
            rowx, colx = i +x, j +y 
            if rowx >= 0 and rowx < len(grid) and colx >= 0 and colx < len(grid[0]) and grid[rowx][colx] == 1:
                grid[rowx][colx] = -1
                queue.append((rowx,colx))
    return grid
    