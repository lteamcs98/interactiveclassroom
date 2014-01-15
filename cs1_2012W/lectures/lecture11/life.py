# life.py
# Plays the Game of Life.
# A colony of cells undergoes generations.
# Each cell is either alive (blue) or dead (yellow).
# In each generation, count the number of living neighbors
# of each cell:
#    If 0 or 1, the cell dies of exposure.
#    If 4 or more, the cell dies of overcrowding.
#    If 3, the cell is revived.
#    If 2, the cell does not change.

from cs1lib import *
from colony import *
from cell import CELL_SIZE

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

# Callback for mouse clicks.  Flips the cell
# at the location of the click, if there's a
# cell there.
def on_click():
    global hive
    hive.flip_cell(mouse_x(), mouse_y())
    
# Callback for key presses.
def on_key_press():
    global timestep
    # If f ("faster") key is pressed, halve the timestep.
    # If s ("slower") key is pressed, double the timestep.
    if is_key_pressed("f"):
        timestep /= 2.0
    elif is_key_pressed("s") and timestep <= 8.0:
        timestep *= 2.0

# Main function for running the game.
def main():
    global hive, timestep
    
    # Create and draw the colony.
    # It should fill the window without going over.
    hive = Colony(WINDOW_HEIGHT / CELL_SIZE,
                  WINDOW_WIDTH / CELL_SIZE)
    hive.draw()
    request_redraw()
    
    # Whenever the mouse is clicked, call on_click.
    set_mouse_button_function(on_click)
    
    # Wait for the space bar to be pressed.
    while not is_key_pressed(" "):
        pass
    
    # Whenever a key is pressed, call on_key_press.
    set_keypress_function(on_key_press)
    
    timestep = 1.0  # seconds

    # Compute a new generation every timestep.
    while not window_closed():
        hive.compute_generation()
        sleep(timestep)    
        
start_graphics(main, "Life", WINDOW_WIDTH, WINDOW_HEIGHT)