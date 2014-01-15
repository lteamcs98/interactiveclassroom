# node_example.py
# CS 1 class example by Devin Balkcom, modified by THC.
# Shows a simple way to use Node objects to form a linked list.

class Node:
    def __init__(self, data):
        self.data = data  # instance variable to store the data
        self.next = None  # instance variable with address of next node

# The head is the first node in a linked list.
head = Node("Maine")

# Create a new node.
another_node = Node("Idaho")

# Store the address of the Idaho node as the
#  next address of the first node in the list.
head.next = another_node

# Create a third node.
a_third_node = Node("Utah")

# Link the second node to the third node.
another_node.next = a_third_node

# An example of printing the data of the list in order:
node = head   # copy the address of the head node into node
while node != None:
    print node.data
    node = node.next
