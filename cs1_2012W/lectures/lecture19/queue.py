# queue.py
# Written by Devin Balkcom
# Shows how to use a Python deque as a queue.

from collections import deque

q = deque()

q.append(5)
q.append(10)
q.append(25)
print q
print "length = ", len(q)

print q.popleft()
print q
print q.popleft()
print q
print q.popleft()
print q
