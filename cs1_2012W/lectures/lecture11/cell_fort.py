# cell.py
# Class for a cell in the Game of Life.

from cs1lib import *

class Cell:
    __CELL_SIZE = 20        # width and height of each cell, in pixels
    
    # Initialize a new Cell.
    def __init__(self, row, column):
        self.__am_living = False
        self.__x = column * Cell.__CELL_SIZE
        self.__y = row * Cell.__CELL_SIZE
    
    # Kill this Cell.
    def kill(self):
        self.__am_living = False
        
    # Make this Cell be alive.
    def revive(self):
        self.__am_living = True
        
    # If this Cell is alive, make it dead.
    # If it's dead, make it alive.
    def flip(self):
        self.__am_living = not self.__am_living
        
    # Return whether this Cell is alive.
    def is_living(self):
        return self.__am_living
        
    # Have a Cell draw itself.
    def draw(self):
        enable_stroke()
        if self.__am_living:
            set_fill_color(0, 0, 1)     # living cells are blue
        else:
            set_fill_color(1, 1, 0)     # dead cells are yellow
            
        set_stroke_color(0, 0, 0)       # black border for all cells

        draw_rectangle(self.__x, self.__y, Cell.__CELL_SIZE, Cell.__CELL_SIZE)
       
    # Return the size of each Cell, in pixels.
    # This is a class method, so it is not called on an instance.
    @classmethod
    def get_cell_size(cls):
        return cls.__CELL_SIZE