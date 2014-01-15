# binary_search.py
# Solution to CS 1 Short Assignment 8 by THC.
# Performs binary search on a sorted list of random numbers.

from random import randint

# Perform binary search for key on the sublist of the_list
# starting at index left and going up to and including index right.
# If key appears in the_list, return the index where it appears.
# Otherwise, return None.
# Requires the_list to be sorted.
def binary_search(the_list, key, left = None, right = None):
    # If using the default parameters, then search the entire list.
    if left == None and right == None:
        left = 0
        right = len(the_list) - 1
    
        # YOU FILL IN THE REST OF THIS FUNCTION.
        
# Driver code for binary search.
n = int(raw_input("How many items in the list? "))

# Make a list of n random ints.
i = 0
the_list = []
while i < n:
    the_list.append(randint(0, 1000))
    i += 1
    
# Binary search wants a sorted list.
the_list = sorted(the_list)
print "The list: " + str(the_list)

while True:
    key = raw_input("What value to search for? ")
    
    if key == "?":
        print "The list: " + str(the_list)
    else:
        key = int(key)    
        index = binary_search(the_list, key)
        if index == None:
            print str(key) + " not found"
        else:
            print str(key) + " found at index " + str(index)