from queue import LifoQueue

"""
array = LifoQueue(maxsize=3)

print(array.empty())

array.put("zero")
array.put("one")
array.put("two")

print(array.full())

print(array.get())
print(array.get())
print(array.get())

# LIFO - Last in First Out
"""

from collections import deque

Queue = deque()

Queue.append("b")
Queue.append("v")
Queue.append("c")

print("init queue", Queue)

print(Queue.popleft())
print(Queue.popleft())
#print(Queue.popleft())

print(list(Queue))