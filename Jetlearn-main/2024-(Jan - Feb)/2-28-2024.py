import heapq

New =  [5, 9, 1, 3, 4, 0]

# Using heapify we can rearange the elements

heapq.heapify(New)

print(New)

# Inserting into heap

heapq.heappush(New, -7)

print(New)

# Removing from heap

heapq.heappop(New)

print(New)

# Replacing an item in heap

heapq.heapreplace(New, 5)

print(New)