# quicksort.py
# Performs the quicksort algorithm.
# Written by THC for CS 1 Lab Assignment 3.

# Swap the items in the_list[i] and the_list[j].
def swap(the_list, i, j):
    temp = the_list[i]
    the_list[i] = the_list[j]
    the_list[j] = temp

# Partition the sublist the_list[p : r+1] so that the pivot
# (originally in the_list[r]) moves to the_list[q],
# all items in the_list[p : q] are less than or equal to the pivot,
# and all items in the_list[q+1 : r+1] are greater than the pivot.
# Return the index q where the pivot ends up.
def partition(the_list, p, r, compare_func):
    pivot = the_list[r]
    
    # Set up the indices i and j so that
    #    the_list[p : i+1] contains items <= pivot,
    #    the_list[i+1 : j] contains items > pivot, and
    #    the_list[j+1 : r] contains items not yet compared with the pivot.
    i = p - 1
    j = p
    while j < r:
        if compare_func(the_list[j], pivot):
            # Move this item into the section known to be <= pivot.
            i += 1
            swap(the_list, i, j)
        j += 1
            
    # Get the pivot into the correct position.
    swap(the_list, i+1, r)
    return i+1

# Sort the sublist the_list[p : r+1] using the quicksort algorithm.
def quicksort(the_list, p, r, compare_func):
    if p < r:   # nothing to do if the sublist has fewer than 2 items
        q = partition(the_list, p, r, compare_func) # divide
        quicksort(the_list, p, q-1, compare_func)   # conquer smaller items
        quicksort(the_list, q+1, r, compare_func)   # conquer larger items

# Sort the_list by running quicksort on it.        
def sort(the_list, compare_func):
    quicksort(the_list, 0, len(the_list)-1, compare_func)
