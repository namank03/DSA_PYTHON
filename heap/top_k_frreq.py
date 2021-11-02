import heapq

a = [1, 1, 1, 3, 2, 2, 4]
heap = []
k = 2
d = {}

for i in a:
    d[i] = d.get(i, 0)
    d[i] += 1
    heapq.heappush(heap, (d[i], i))
    if len(heap) > k:
        heapq.heappop(heap)

print(f'heap -> {heap}')
