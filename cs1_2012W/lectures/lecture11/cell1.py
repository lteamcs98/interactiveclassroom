# cell.py
# Class for a cell in the Game of Life.
# CS 1 class example by THC.

from cs1lib import *

CELL_SIZE = 20  # width and height of each cell, in pixels

class Cell:    
    # Initialize a new Cell.
    def __init__(self, row, column):
        self.am_living = False
        self.x = column * CELL_SIZE
        self.y = row * CELL_SIZE
    
    # Kill this Cell.
    def kill(self):
        self.am_living = False
        
    # Make this Cell be alive.
    def revive(self):
        self.am_living = True
        
    # Return whether this Cell is alive.
    def is_living(self):
        return self.am_living
            
    # If this Cell is alive, make it dead.  If it's dead, make it alive.
    def flip(self):
        self.am_living = not self.am_living

    # Have a Cell draw itself.
    def draw(self):
        if self.am_living:
            set_fill_color(0, 0, 1)     # living cells are blue
        else:
            set_fill_color(1, 1, 0)     # dead cells are yellow
            
        set_stroke_color(0, 0, 0)       # black border for all cells

        draw_rectangle(self.x, self.y, CELL_SIZE, CELL_SIZE)
