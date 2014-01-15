# sentinel_DLL.py
# CS 1 class example for a circular, doubly linked list with a sentinel.
# Written by Devin Balkcom, modified by THC.

# Class for a node in a circular, doubly linked list with a sentinel.
class Node:
    def __init__(self, data):
        self.data = data  # instance variable to store the data
        self.next = None  # instance variable with address of next node
        self.prev = None  # instance variable with address of previous node

# Class for a circular, doubly linked list with a sentinel.
class Sentinel_DLL:
    # Create the sentinel node, which is before the first node
    # and after the last node.
    def __init__(self):        
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        
    # Return a reference to the first node in the list, if there is one.
    # If the list is empty, return None.
    def first_node(self):
        if self.sentinel.next == self.sentinel:
            return None
        else:
            return self.sentinel.next
    
    # Insert a new node with data after node x.
    def insert_after(self, x, data):
        y = Node(data)   # make a new Node object.

        # Fix up the links in the new node.
        y.prev = x
        y.next = x.next
        
        # The new node follows x.
        x.next = y
        
        # And it's the previous node of its next node.
        y.next.prev = y
    
    # Insert a new node at the end of the list.    
    def append(self, data):
        last_node = self.sentinel.prev
        self.insert_after(last_node, data)
    
    # Delete node x from the list.
    def delete(self, x):
        # Splice out node x by making its next and previous
        # reference each other.
        x.prev.next = x.next
        x.next.prev = x.prev
    
    # Find a node containing data, and return a reference to it.
    # If no node contains data, return None.
    def find(self, data):
        # Trick: Store a copy of the data in the sentinel,
        # so that the data is always found.  
        self.sentinel.data = data
        
        x = self.first_node()
        while x.data != data:
            x = x.next
            
        # Restore the sentinel's data.
        self.sentinel.data = None
        
        # Why did we drop out of the while-loop?
        # If we found the data in the sentinel, then it wasn't
        # anywhere else in the list.
        if x == self.sentinel:
            return None     # data wasn't really in the list
        else:
            return x        # we found it in x, in the list
        
    
    # Return the string representation of a circular, doubly linked
    # list with a sentinel, just as if it were a Python list.
    def __str__(self):
        s = "["

        x = self.sentinel.next
        while x != self.sentinel: # look at each node in the list
            if type(x.data) == str:
                s += "'"
            s += str(x.data)        # concatenate this node's data to the string
            if type(x.data) == str:
                s += "'"
            if x.next != self.sentinel:
                s += ", "   # if not the last node, add the comma and space
            x = x.next

        s += "]"        
        return s
