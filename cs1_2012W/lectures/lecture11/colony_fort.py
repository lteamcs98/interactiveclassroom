# colony.py
# Class for a colony of cells in the Game of Life.
# CS 1 class example by THC.

from cell import *
from cs1lib import *

class Colony:
    # The instance variable __cells is a list of references to rows,
    # and each row is a list of references to Cell objects.
    
    # Create a colony with a given number of rows and columns.
    def __init__(self, rows, columns):
        # Remember the number of rows and columns.
        self.__rows = rows
        self.__columns = columns
        
        # Create __cells as a list of references to rows.
        self.__cells = [None] * rows
        
        for row in range(rows):
            # Create a row of new Cell objects.
            self.__cells[row] = [None] * columns
            for column in range(columns):
                self.__cells[row][column] = Cell(row, column)
            
    # Draw a colony of cells.
    def draw(self):
        # Draw each row of cells.
        for row in range(self.__rows):
            # Have each Cell in this row draw itself.
            for column in range(self.__columns):
                self.__cells[row][column].draw()

    # Called when a click occurs.
    def flip_cell(self, x, y):
        # Compute the row and column corresponding to the mouse position.
        row = y / Cell.get_cell_size()
        column = x / Cell.get_cell_size()
        
        # If within the colony, flip the cell at that row and column.
        if (0 <= row < self.__rows) and (0 <= column < self.__columns):
            self.__cells[row][column].flip()
            self.__cells[row][column].draw()
            request_redraw()
            
    # Compute the next generation of cells.
    def compute_generation(self):
        # Initialize a list of lists of counts of living neighbors.
        living_neighbors = [None] * self.__rows
        for row in range(self.__rows):
            living_neighbors[row] = [0] * self.__columns
        
        # Go through the entire colony, incrementing the living neighbor
        # count of each neighbor of each living cell.
        for row in range(self.__rows):
            for column in range(self.__columns):
                if self.__cells[row][column].is_living():
                    # It's living, so increment, wrapping around as necessary.
                    row_above = (row - 1) % self.__rows
                    row_below = (row + 1) % self.__rows
                    column_left = (column - 1) % self.__columns
                    column_right = (column + 1) % self.__columns
                    living_neighbors[row_above][column_left] += 1
                    living_neighbors[row_above][column] += 1
                    living_neighbors[row_above][column_right] += 1
                    living_neighbors[row][column_left] += 1
                    living_neighbors[row][column_right] += 1
                    living_neighbors[row_below][column_left] += 1
                    living_neighbors[row_below][column] += 1
                    living_neighbors[row_below][column_right] += 1
                    
        # Now go back through the entire colony, killing cells with too few
        # or too many living neighbors, and making cells with 3 living neighbors
        # be alive.
        for row in range(self.__rows):
            for column in range(self.__columns):
                if (living_neighbors[row][column] <= 1) or \
                    (living_neighbors[row][column] >= 4):
                    self.__cells[row][column].kill()
                elif living_neighbors[row][column] == 3:
                    self.__cells[row][column].revive()
        
        # Having updated the entire colony, redraw it.
        clear()
        self.draw()
        request_redraw()
        