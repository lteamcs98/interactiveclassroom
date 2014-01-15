# circle_paint2.py
# Devin Balkcom
# September 2011

from cs1lib import *
from random import uniform

def main():
    enable_smoothing()
    clear()
    
    # Set up state variables that will store the coordinates
    # of the mouse from the last time a circle was drawn.
    old_x = -1
    old_y = -1

    while not window_closed():
        # Draw a circle ONLY if the current mouse location is different
        # from where it was the last time a circle was drawn.
        if mouse_down() and (old_x != mouse_x() or old_y != mouse_y()):
            # Pick a circle color at random
            r = uniform(.5, 1)
            g = uniform(.5, 1)
            b = uniform(.5, 1)
            set_fill_color(r, g, b)

            # Draw the circle.
            draw_circle(mouse_x(), mouse_y(), 20)
            
            # Store the current mouse coordinates into the state variables.
            old_x = mouse_x()
            old_y = mouse_y()

            # Update the window.
            # We have to save the current mouse location BEFORE sleeping.
            request_redraw()
            sleep(.02)

start_graphics(main)