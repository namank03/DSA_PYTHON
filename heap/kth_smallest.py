# nlon to n logk
# Reverse options if asked for smallest element create max heap and if asked for largest element create min heap
# [7 10 4 3 20 15]
# Visualize as stack if creating max heap then element at the top will be max. WE'll iterate through the array and checking the heap size on each iterations.
# to implement a max heap in python just multiply the elements by -1 and there you go

import heapq

a = [10, 2, 13, 14, 15, 1, 3]
heap = []
k = 4

for i in a:
    heapq.heappush(heap, i)
    if len(heap) > k:
        heapq.heappop(heap)

print(f'heap -> {heap}')
