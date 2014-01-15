# List reverse example for cs1
# Devin Balkcom
# August 2011 

# An example list
l = [1, 3, 5, 7, 9, 11, 13, 15]

print "The list before reversing:  " + str(l)

index = 0
while index < len(l) / 2:
    # We'll call the index of the item to swap with the right_index,
    # since it's the index into the right half of the list.

    # Because indices start at 0, the last item of the list is at 
    # index len(l) - 1.
    right_index = len(l) - 1 - index

    # Swap the items at index and right_index.
    temp = l[index]  # store the value at l[index] before clobbering
    l[index] = l[right_index]
    l[right_index] = temp

    index = index + 1
    
print "The list after reversing:  " + str(l)
