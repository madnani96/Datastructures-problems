import heapq
'''

data = [5, 7, 9, 1, 3]
heapq.heapify(data)

print(data,"after heapify")  # This will output [1, 3, 9, 7, 5], which is a heap.



heapq.heappush(data, 4)
print(data, "pushed 4")  # This will output [1, 3, 4, 7, 5, 9], which is still a heap.

print(heapq.heappop(data))  # This will output 1, the smallest element in the heap.
print(data)  

print(heapq.heappop(data))
print(heapq.heappop(data))
print(heapq.heappop(data))
print(heapq.heappop(data))
print(heapq.heappop(data))


print(data)


print(heapq.heapreplace(data, 6))  # This will output 3, the smallest element in the original heap.
print(data)  # This will output [4, 5, 6, 7, 9], which is still a heap.


#max heap


import heapq

data = [5, 7, 9, 1, 3]

# Convert elements to negative values before pushing onto the heap
heap = [-x for x in data]

# Use heapify to create a max-heap
heapq.heapify(heap)
print(heap)
'''
# Multiply elements by -1 when retrieving from the heap to get the original values
#print([ -x for x in heap])  # This will output [9, 7, 5, 1, 3], which is a max-heap.



data=[]
heapq.heapify(data)
heapq.heappush(data,10)
heapq.heappush(data,20)
heapq.heappush(data, 30)
heapq.heappush(data, 40)

heapq.heappop(data)


print(data)

heapq.heapreplace(data,15)
print(data)