# colony.py
# Class for a colony of cells in the Game of Life.

from cell import *
from cs1lib import *

class Colony:
    # Create a colony, with a given number of rows and columns.
    def __init__(self, rows, columns):
        # Remember the number of rows and columns.
        self.rows = rows
        self.columns = columns
        
        # Create cells as a reference to a list of references to rows.
        self.cells = [None] * rows
        
        for row in range(rows):
            # Create a row of references to Cell objects.
            self.cells[row] = [None] * columns
            for column in range(columns):
                self.cells[row][column] = Cell(row, column)
                
    # Draw a colony of cells.
    def draw(self):
        # Draw each row of cells.
        for row in range(self.rows):
            # Have each cell in this row draw itself.
            for column in range(self.columns):
                self.cells[row][column].draw()
                
    # Called when a click occurs.
    def flip_cell(self, x, y):
        # Compute the row and column number corresponding to the mouse position.
        row = y / CELL_SIZE
        column = x / CELL_SIZE
        
        if (0 <= row < self.rows) and (0 <= column < self.columns):
            self.cells[row][column].flip()
            self.cells[row][column].draw()
            request_redraw()
            
    # Compute the next generation of cells.
    def compute_generation(self):
        # Initialize a list of lists of counts of living neighbors.
        living_neighbors = [None] * self.rows
        for row in range(self.rows):
            living_neighbors[row] = [0] * self.columns
            
        # Go through the entire colony, incrementing the living neighbor
        # count of each neighbor of each living cell.
        for row in range(self.rows):
            for column in range(self.columns):
                if self.cells[row][column].is_living():
                    # It's living, so increment.
                    row_above = (row-1) % self.rows
                    row_below = (row+1) % self.rows
                    column_left = (column-1) % self.columns
                    column_right = (column+1) % self.columns
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
        for row in range(self.rows):
            for column in range(self.columns):
                if (living_neighbors[row][column] <= 1) or \
                    (living_neighbors[row][column] >= 4):
                    self.cells[row][column].kill()
                elif living_neighbors[row][column] == 3:
                    self.cells[row][column].revive()
                    
        # Having updated the entire colony, redraw it.
        clear()
        self.draw()
        request_redraw()
        