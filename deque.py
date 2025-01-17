from collections import deque

# Create a deque
queue = deque()
queue.append("data 1")
queue.append("data 2")  
queue.append("data 3")
print(queue)
# deque(['data 1', 'data 2', 'data 3'])

first_item = queue.popleft()
print(first_item)