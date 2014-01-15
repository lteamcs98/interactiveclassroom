from cs1lib import *
from colony import *

def on_click():
    global hive
    hive.flip_cell(mouse_x(), mouse_y())

def main():
    global hive
    hive = Colony(10, 10)
    hive.draw()
    request_redraw()
    set_mouse_button_function(on_click)
    
    # Wait for the space bar to be pressed.
    while not is_key_pressed(" "):
        pass

    while not window_closed():
        hive.compute_generation()
        sleep(1)    
        
start_graphics(main)