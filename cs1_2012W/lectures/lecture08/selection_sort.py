grade_list = [89, 45, 85, 81, 77, 94, 22, 79, 92, 91]
print "grade_list before sorting: ", grade_list

# Selection sort algorithm pseudo-code:
#   for each consecutive index i in the list:
#     find the minimum value in the sublist starting at index i.
#     call the index of this value index_smallest.  
#     swap the items at indices i and index_smallest.

for i in range(len(grade_list) - 1):
    # Find the minimum value in the sublist starting at index i.
    # minval will hold the smallest value we have found so far in the sublist
    minval = grade_list[i]
    index_smallest = i

    for j in range(i, len(grade_list)):
        if grade_list[j] < minval:
            minval = grade_list[j]
            index_smallest = j

    # After the inner loop, minval has the smallest value in the sublist
    # starting at index i, and index_smallest has the index of this
    # smallest value.  Swap it into index i.
    temp = grade_list[i]
    grade_list[i] = minval
    grade_list[index_smallest] = temp

print "grade_list after sorting:  ", grade_list
