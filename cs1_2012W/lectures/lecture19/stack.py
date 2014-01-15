# stack.py
# Written by Devin Balkcom for CS 1.
# Shows how to use a Python list as a stack.

stack = []
print stack

stack.append(5)
print "pushed 5"
print stack

stack.append(2)
print "pushed 2"
print stack

stack.append(4)
print "pushed 4"
print stack

print "popped:", stack.pop()
print stack

stack.append(19)
print "pushed 19"
print stack

stack.append(11)
print "pushed 11"
print stack

print "popped:", stack.pop()
print stack
print "popped:", stack.pop()
print stack
print "popped:", stack.pop()
print stack
print "popped:", stack.pop()
print stack
