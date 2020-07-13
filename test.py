from collections import deque
q = deque()
q.append(6)
q.append(5)
q.append(7)
print(q)
q.popleft()
q.popleft()
q.popleft()
print(q)
if q:
    print("yes")
