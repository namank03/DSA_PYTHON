import heapq

a = [5, 6, 7, 8, 9]
k = 3
x = 7
heap = []
#  [-2,-1,0,1,2]

for index, val in enumerate(a):
    heapq.heappush(heap, (-abs(val-x), index))
    if len(heap) > k:
        el, index = heapq.heappop(heap)
        print(f'el -> {el}')
        print(f'index -> {index}')

print(f'heap -> {heap}')
