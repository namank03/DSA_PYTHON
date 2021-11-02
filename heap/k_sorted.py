import heapq

a = [6, 5, 3, 2, 8, 9, 10]
k = 3
heap = []

l = []
for i in a:
    if len(heap) < k:
        heapq.heappush(heap, i)
    else:
        l.append(heapq.heappushpop(heap, i))

l += heap

print(f'l -> {l}')
