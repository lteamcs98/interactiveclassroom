# sort_states.py
# Solution to CS 1 Short Assignment 10 by THC.
# Reads in a file of US states, sorts it, and writes it
# out to a file, five states per line.

from merge_sort import merge_sort

LINE_LENGTH = 5     # number of states per line in output file

in_file = open("states.txt", "r")    # open for reading
states = []     # list of names of states

for line in in_file:
    for state in line.split(','):   # get each comma-separated item
        if len(state.strip()) > 0:  # anything left after stripping off whitespace?
            states.append(state.strip())    # if yes, append to states
    
in_file.close() # done reading from the file, so close it

states.sort()   # sort the states

out_file = open("sorted_states.txt", "w")    # open for writing
count = 0   # how many written so far

for state in states:
    out_file.write(state)
    if count % LINE_LENGTH == LINE_LENGTH - 1:
        out_file.write("\n")     # end of line
    else:
        out_file.write(", ")     # not end of line
    count += 1
    
out_file.close() # done writing to the file, so close it

