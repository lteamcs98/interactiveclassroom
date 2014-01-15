the_list = [89, 45, 85, 81, 77, 94, 22, 77, 92, 91]

def insertion_sort(the_list):
    n = len(the_list)   # how many items to sort
    
    for i in range (1, n):
        key = the_list[i]   # remember what was in the ith position
        
        # Search from right to left through the sublist to the left of
        # the_list[i].  Move each item one position to the right if we
        # find that the key goes somewhere before it.  Stop if we run
        # off the beginning of the list or once we find an item for which
        # the key does not go before it.
        j = i-1     # look in positions to the left of i        
        while j >= 0 and the_list[j] > key:
            the_list[j+1] = the_list[j]
            j -= 1
            
        # Either j == -1 and we want to put key at the_list[0], or
        # j >= 0 and key >= the_list[j], so we want to put key at
        # the_list[j+1].
        the_list[j+1] = key
        
insertion_sort(the_list)

print the_list
