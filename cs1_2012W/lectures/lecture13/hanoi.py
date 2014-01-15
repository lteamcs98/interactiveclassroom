# Hanoi.py
# Originally by Scot Drysdale
#  Translated into Python by Devin Balkcom.
#  Minor changes by THC.
#  Solves the Towers of Hanoi puzzle.

def move_disk(disk_number, from_peg, to_peg):
    print "Move disk " + str(disk_number) + " from peg " \
        + str(from_peg) + " to peg " + str(to_peg) + "."    

def solve_hanoi(n, start_peg, end_peg):
    if n == 1:
        # Base case: Move a "tower" of height 1 by simply moving
        # the only disk.
        move_disk(n, start_peg, end_peg)
    else:   # recursive case
        # A trick to compute the number of the spare peg:  1 + 2 + 3 = 6.
        spare_peg = 6 - start_peg - end_peg  
        
        # Move all but the bottom disk from start peg to spare peg.
        solve_hanoi(n - 1, start_peg, spare_peg) 
    
        # Move the bottom disk from the start peg to the end peg.
        move_disk(n, start_peg, end_peg)
        
        # Move all but the bottom disk from spare peg to end peg.
        solve_hanoi(n - 1, spare_peg, end_peg)
    
solve_hanoi(5, 1, 2)