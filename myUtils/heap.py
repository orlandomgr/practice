import heapq

heap = [1,2,3]
heapq.heapify(heap)

heapq.heappush(heap, 4)
value = heapq.heappop(heap)
print(value)

